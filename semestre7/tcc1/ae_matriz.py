import struct
import time
from numba import njit # Incompatível com classes, sendo necessário a utilização de funções auxiliares para algumas funções
import numpy as np

class INDIVIDUO:
    #__init__ é um método construtor que inicializa os atributos dos objetos
    def __init__(self, fitness = 0, matriz = None):
        self.fitness = fitness # Número de caracteres distintos entre a matriz alvo e a matriz cópia (quanto menor melhor)
        self.matriz = matriz # Matriz contendo as nove 'submatrizes'


class PARAMETROS:
    def __init__(self, matrizAlvo = None, numerosValidos = None, populacao = 0, geracoes = 0, elitismo = 0, mutacao = 0, torneio = 0):
        self.matrizAlvo = matrizAlvo # Matriz alvo
        self.numerosValidos = numerosValidos # Números válidos (1-9) para o Sudoku
        self.populacao = populacao # Tamanho da população
        self.geracoes = geracoes # Número de gerações
        self.elitismo = elitismo # Taxa de elitismo (1 a 100)
        self.mutacao = mutacao # Taxa de mutação (1 a 100)
        self.torneio = torneio # Número de participantes da seleção por torneio

'''
    Função escreveArquivo:
        Escreve no arquivo entrada.in a frase alvo e os parâmetros especificados.
'''
def escreveArquivo():
    populacao = 600
    geracoes = 1800
    mutacao = 15
    elitismo = 5
    torneio = 3

    matrizAlvo = np.block([[3,4,2, 5,6,8, 1,9,7], 
                           [6,8,7, 9,1,3, 2,5,4], 
                           [9,5,1, 4,7,2, 6,3,8], 
                           [9,2,6, 8,5,1, 4,7,3],
                           [3,4,5, 7,2,6, 8,9,1], 
                           [8,1,7, 3,9,4, 2,6,5], 
                           [6,8,5, 7,3,4, 2,1,9], 
                           [4,7,9, 1,6,2, 5,3,8], 
                           [1,2,3, 5,8,9, 7,4,6]])
    
    try:
        # Gera o arquivo entrada.in para escrita
        with open('entrada.in', 'wb') as arquivo:
            arquivo.write(populacao.to_bytes(4, byteorder='big')) 
            arquivo.write(geracoes.to_bytes(4, byteorder='big'))
            arquivo.write(mutacao.to_bytes(4, byteorder='big'))
            arquivo.write(elitismo.to_bytes(4, byteorder='big'))
            arquivo.write(torneio.to_bytes(4, byteorder='big'))
            np.save(arquivo, matrizAlvo) # Salva a matriz alvo no arquivo
        # Estrutura with fecha o arquivo automaticamente
    except Exception as e: # Caso haja erro na criação do arquivo metricas.in
        print(f"Problemas na criação do arquivo {e}\n")

'''
    Função escreveRelatorio:
        Escreve no arquivo relatorio.txt o tempo de execução do programa e o fitness 
        do melhor indivíduo obtido.
    Parâmetros: 
        tempo - tempo gasto na execução do programa.
        fitness - quantidade de caracteres (números) distintos entre a matriz alvo e o indivíduo mais adaptado da População.
    Retorno:
        Nulo.
'''
def escreveRelatorio(tempo, fitness):
    try:
        # Gravando os dados no arquivo relatorio.txt
        with open('relatorio.txt', 'a') as arquivo, open('metricas.in', 'ab') as binario:
            arquivo.write(f'{tempo:.3f}')
            arquivo.write(f'{fitness:.3f}')
            binario.write(struct.pack("d", tempo))
            binario.write(struct.pack("f", fitness))
    except Exception as e: # Caso haja erro na criação do arquivo relatorio.txt
        print(f"Problemas na criação do arquivo {e}\n")
    
    try:
        with open('relatorio.txt', 'r') as arquivo:
            resultado = arquivo.read()
            if not resultado:
                print("Erro na gravação")
    except FileNotFoundError as e:
        print(f"Arquivo {e} não foi encontrado.\n")

'''
    Função leArquivo:
        Lê no arquivo entrada.in com os parâmetros definidos pelo usuário
        para os testes.
    Retorno:
        Instância da classe PARAMETROS com os parâmetros lidos.
'''
def leArquivo():
    try:
        parametros = PARAMETROS()
        # Lê o arquivo entrada.in
        with open('entrada.in', 'rb') as arquivo:
            populacao = arquivo.read(4) 
            geracoes = arquivo.read(4)
            mutacao = arquivo.read(4)
            elitismo = arquivo.read(4)
            torneio = arquivo.read(4)
            matrizAlvo = np.load(arquivo) # Lê a matriz alvo do arquivo

            parametros.populacao = int.from_bytes(populacao, byteorder='big')
            parametros.geracoes = int.from_bytes(geracoes, byteorder='big')
            parametros.mutacao = int.from_bytes(mutacao, byteorder='big')
            parametros.elitismo = int.from_bytes(elitismo, byteorder='big')
            parametros.torneio = int.from_bytes(torneio, byteorder='big')
            parametros.matrizAlvo = matrizAlvo
    
    except FileNotFoundError as e:
        print(f"Arquivo {e} não foi encontrado.\n")    

    return parametros

'''
    Função fitness:
        Calcula o fitness de um indivíduo baseado no número de caracteres (números) distintos entre 
        a matriz alvo e a matriz cópia. Quanto menor o número de caracteres distintos, melhor 
        o fitness.
    Parâmetros: 
        matriz - matriz do indivíduo a ser avaliado.
        matrizAlvo - matriz alvo.
    Retorno:
        Número de caracteres distintos entre a matriz alvo e a matriz cópia.
'''
@njit
def fitness(matriz, matrizAlvo):
    matrizUnidimensional = matriz.flatten() # .flatten() converte a matriz em um array unidimensional
    matrizAlvoUnidimensional = matrizAlvo.flatten()
    quantidadeDistintos = 0

    tamanho = len(matrizUnidimensional) if len(matrizUnidimensional) == len(matrizAlvoUnidimensional) else min(len(matrizUnidimensional), len(matrizAlvoUnidimensional))

    for i in range(tamanho):
        if matrizUnidimensional[i] != matrizAlvoUnidimensional[i]:
            quantidadeDistintos += 1

    # Caso haja algum indivíduo com uma matriz de tamanho inesperado:
    quantidadeDistintos += abs(len(matrizUnidimensional) - len(matrizAlvoUnidimensional))

    return quantidadeDistintos

'''
    Função mutacaoAuxiliar:
        Altera aleatoriamente um gene (número) da matriz do filho, substituindo-o
        por um valor aleatório correspondente a um dos caracteres presentes no intervalo
        numérico da matriz alvo.
    Parâmetros:
        matriz - matriz do indivíduo a ser avaliado.
        taxaMutacao - taxa de mutação (1 a 100).
        numerosValidos - número de caracteres disponíveis para a mutação.
    Retorno:
        Matriz após ser mutada.
'''
@njit
def mutacaoAuxiliar(matriz, taxaMutacao, numerosValidos):
    # Matriz auxiliar
    novaMatriz = matriz.flatten().copy()
    
    # Verifica se ocorrerá mutação baseado na taxa
    if np.random.randint(0, 100) < taxaMutacao:
        posicao = np.random.randint(len(novaMatriz))
        novoValor = np.random.choice(numerosValidos) # Escolhe um valor aleatório da matriz original
        novaMatriz[posicao] = novoValor
        
    return novaMatriz # Retorna matriz unidimensional mutada

'''
    Função mutacao:
        Utiliza a função mutacaoAuxiliar para realizar a mutação de um indivíduo.
    Parâmetros:
        filho - um dos indivíduos da população.
        parametros - classe PARAMETROS.
    Retorno:
        Indivíduo mutado.
'''
def mutacao(filho, parametros):
    individuo = INDIVIDUO(filho.fitness, filho.matriz)

    # Certifica que a matriz do filho não é None
    if filho.matriz is None:
        return INDIVIDUO(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Realiza a mutação da matriz unidimensional do filho
    matrizMutada = mutacaoAuxiliar(filho.matriz, parametros.mutacao, parametros.numerosValidos)
    
    individuo.matriz = matrizMutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo

'''
    Função recombinacaoUniformeAuxiliar:
        Combina aleatoriamente os genes da matriz pai e mãe no filho.
    Parâmetros:
        matrizPai - matriz do pai.
        matrizMae - matriz da mãe.
        tamanho - tamanho da matriz alvo.
    Retorno:
        Matriz do filho resultante da combinação entre pai e mãe.
'''
@njit
def recombinacaoUniformeAuxiliar(matrizPai, matrizMae, tamanho):
    matrizPaiUnidimensional = matrizPai.flatten()
    matrizMaeUnidimensional = matrizMae.flatten()
    comprimentoMax = min(len(matrizPaiUnidimensional), len(matrizMaeUnidimensional), tamanho)
    filho = np.empty(comprimentoMax, dtype=matrizPaiUnidimensional.dtype)
    
    for i in range(comprimentoMax):
        if np.random.randint(0, 2) == 1:
            filho[i] = matrizPaiUnidimensional[i]
        else:
            filho[i] = matrizMaeUnidimensional[i]
            
    return filho # Retorna filho como array unidimensional                                                                                                                                          

'''
    Função recombinacaoUniforme:
        Utiliza a função recombinacaoUniformeAuxiliar para realizar a recombinação entre pai e mãe.
    Parâmetros:
        pai - um dos indivíduos da população.
        mae - um dos indivíduos da população.
        numero - tamanho da matriz alvo.
    Retorno:
        Indivíduo filho resultante da combinação entre pai e mãe.
'''
def recombinacaoUniforme(pai, mae, numero):
    filho = INDIVIDUO()

    # Certifica que os pais têm representação de array
    if pai.matriz is None or mae.matriz is None:
        return INDIVIDUO() # Retorna indivíduo vazio

    # Realiza a recombinação da matriz unidimensional do filho
    matrizFilho = recombinacaoUniformeAuxiliar(pai.matriz, mae.matriz, numero)
    
    filho.matriz = matrizFilho.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return filho

'''
    Função selecaoPorTorneio:
        Seleciona dois a dois indivíduos da população e determina qual deles possui o menor fitness.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
        parametros - classe PARAMETROS.
    Retorno:
        Retorna o indivíduo com o menor fitness entre os selecionados.
'''
def selecaoPorTorneio(populacao, parametros):
    melhor = INDIVIDUO()
    melhor.fitness = -1

    for i in range(parametros.torneio):
        auxiliar = populacao[np.random.randint(0, parametros.populacao)]
        if melhor.fitness == -1 or auxiliar.fitness < melhor.fitness:
            melhor = auxiliar

    return melhor

'''
    Função elitismo:
        Calcula o número de indivíduos da população que não sofreram ação dos operadores de mutação 
        e recombinação na função reprodução e ordena por adaptação (indivíduos mais adaptados 
        ocupam posições iniciais).
    Parâmetros:
        população - população de indivíduos (matrizes cópias).
        parametros - classe PARAMETROS.
    Retorno:
        Número de indivíduos selecionados.
'''
def elitismo(populacao, parametros):
    selecionados = parametros.populacao * parametros.elitismo // 100
    populacao.sort(key=lambda individuo: individuo.fitness)
    
    return selecionados

'''
    Função reproducao:
        Aplica as funções de elitismo, torneio, recombinação e mutação na população.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
        parametros - classe PARAMETROS.
    Retorno:
        Retorna o melhor indivíduo da população.
'''
def reproducao(populacao, parametros):
    melhor = INDIVIDUO()
    pai = INDIVIDUO()
    mae = INDIVIDUO()
    filho = INDIVIDUO()
    novaPopulacao = [INDIVIDUO() for _ in range(parametros.populacao)]

    taxaDeElitismo = elitismo(populacao, parametros)

    melhor = INDIVIDUO(fitness=populacao[0].fitness, matriz=np.copy(populacao[0].matriz))

    tamanhoAlvo = len(parametros.matrizAlvo.flatten())

    for i in range(taxaDeElitismo):
        novaPopulacao[i] = INDIVIDUO(populacao[i].fitness, np.copy(populacao[i].matriz))

    for i in range(taxaDeElitismo, parametros.populacao):
        pai = selecaoPorTorneio(populacao, parametros)
        mae = selecaoPorTorneio(populacao, parametros)
        filho = recombinacaoUniforme(pai, mae, tamanhoAlvo)
        filho = mutacao(filho, parametros)
        filho.fitness = fitness(filho.matriz, parametros.matrizAlvo)

        novaPopulacao[i] = filho
        
        if filho.fitness < melhor.fitness:
            melhor = INDIVIDUO(fitness=filho.fitness, matriz=np.copy(filho.matriz))

    for i in range(parametros.populacao):
        populacao[i] = novaPopulacao[i]

    return melhor

'''
    Função geraMatrizesAleatorias:
        Gera matrizes aleatórias de tamanho definido, utilizando os caracteres disponíveis
        no intervalo numérico.
    Parâmetros:
        tamanhoPopulacao - número de matrizes a serem geradas.
        numerosValidos - número de caracteres distintos na matriz alvo.
    Retorno:
        Lista de matrizes aleatórias geradas.
'''
@njit
def geraMatrizesAleatorias(tamanhoPopulacao, numerosValidos):
    
    # Caso os números válidos sejam uma lista vazia, retorna uma matriz de zeros
    if len(numerosValidos) == 0:
        return np.zeros((tamanhoPopulacao, 9, 9), dtype=np.int64)

    matrizes = np.empty((tamanhoPopulacao, 9, 9), dtype=numerosValidos.dtype)
    for i in range(tamanhoPopulacao):
        matrizes[i, :, :] = np.random.choice(numerosValidos, size=(9, 9))

    return matrizes

'''
    Função inicializa:
        Utiliza a função geraMatrizesAleatorias para inicializar a população com matrizes 
        aleatórias de tamanho definido e calcula o fitness de cada uma delas.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
        parametros - classe PARAMETROS.
    Retorno:
        Nulo.
'''

def inicializa(populacao, parametros):
    intervaloNumeros = parametros.numerosValidos
    tamanhoPopulacao = parametros.populacao
    
    matrizesGeradas = geraMatrizesAleatorias(tamanhoPopulacao, intervaloNumeros)
    
    for i in range(tamanhoPopulacao):
        populacao[i] = INDIVIDUO()
        populacao[i].matriz = matrizesGeradas[i]
        populacao[i].fitness = fitness(populacao[i].matriz, parametros.matrizAlvo)
        
'''
    Função intervaloNumeros:
        Determina quais caracteres compõem a matriz alvo.
    Parâmetros:
        parametros - classe PARAMETROS.
    Retorno:
        Retorna a classe PARAMETROS com os números válidos.
'''
def intervaloNumeros(parametros):
    
    if parametros.matrizAlvo is not None:
        numerosDistintos = np.unique(parametros.matrizAlvo.flatten())
        parametros.numerosValidos = numerosDistintos.astype(np.int64)
    else:
        # Fallback importante se matrizAlvo não estiver definida
        print("Aviso: matrizAlvo não definida. Usando números padrão 1-9 para Sudoku.")
        parametros.numerosValidos = np.arange(1, 10, dtype=np.int64) # 1 a 9

    return parametros

'''
    Função setSeed: 
        Define uma semente para o gerador de números aleatórios usado pela biblioteca
        numba, permitindo reprodutibilidade nos testes.
    Parâmetros:
        seed - semente a ser definida.
    Retorno:
        Nulo.
'''
'''@njit
def setSeed(seed):
    np.random.seed(seed)'''

'''
    Função main:
        Implementa o Algoritmo Evolutivo para o problema: dada uma frase alvo,
        reproduza-a através de uma população de frases cópias geradas aleatoriamente.
'''

def main():
    #np.random.seed(0) # Semente fixa para testes
    #setSeed(0) # Semente fixa para testes
    
    inicio = time.time()

    escreveArquivo()
    parametros = leArquivo()
    parametros = intervaloNumeros(parametros)

    geracao = 0
    populacao = [INDIVIDUO() for _ in range(parametros.populacao)]

    np.random.seed(int(time.time())) # Semente de acordo com o tempo de máquina
    inicializa(populacao, parametros)
    while geracao <= parametros.geracoes:
        melhor = reproducao(populacao, parametros)
        print(f"\nIteracao {geracao}, melhor fitness {melhor.fitness}.\n")
        print(f"{melhor.matriz}\n")
        geracao += 1
        if melhor.fitness == 0:
            break

    fim = time.time()
    total = fim - inicio
    print(f"Tempo total gasto pela CPU: {total}")
    escreveRelatorio(total, melhor.fitness)

if __name__ == "__main__":
    main()