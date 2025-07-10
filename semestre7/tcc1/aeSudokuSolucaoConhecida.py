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
    def __init__(self, numerosValidos = None, matrizBase = None, celulasVazias = None, celulasVazias1d = None, 
                populacao = 0, geracoes = 0, elitismo = 0, mutacao = 0, torneio = 0):
        self.numerosValidos = numerosValidos # Números válidos (1-9) para o Sudoku
        self.matrizBase = matrizBase # Matriz base
        self.celulasVazias = celulasVazias # Posições das células vazias na matriz base
        self.celulasVazias1d = celulasVazias1d # Posições das células vazias na matriz base em formato unidimensional
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
    mutacao = 1
    elitismo = 5
    torneio = 3

    matrizBase = np.block([[0,8,4, 0,7,2, 1,0,5], 
                           [2,0,7, 8,3,0, 9,0,0], 
                           [6,0,0, 5,0,9, 0,0,8], 
                           [0,6,0, 9,2,8, 4,0,0],
                           [0,7,0, 0,0,0, 0,6,9], 
                           [0,2,0, 0,0,0, 0,8,1], 
                           [0,3,2, 0,5,0, 6,9,4], 
                           [7,0,0, 0,0,0, 0,0,2], 
                           [1,0,0, 2,0,4, 0,0,7]])
    
    celulasVazias = np.argwhere(matrizBase == 0) # Posições das células vazias na matriz base
    celulasVazias1d = np.where(matrizBase.flatten() == 0)[0] # Posições das células vazias na matriz base em formato unidimensional
    numerosValidos = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Números válidos para o Sudoku
    
    try:
        # Gera o arquivo entrada.in para escrita
        with open('entrada.in', 'wb') as arquivo:
            arquivo.write(populacao.to_bytes(4, byteorder='big')) 
            arquivo.write(geracoes.to_bytes(4, byteorder='big'))
            arquivo.write(mutacao.to_bytes(4, byteorder='big'))
            arquivo.write(elitismo.to_bytes(4, byteorder='big'))
            arquivo.write(torneio.to_bytes(4, byteorder='big'))
            np.save(arquivo, numerosValidos) # Salva os números válidos no arquivo
            np.save(arquivo, matrizBase) # Salva a matriz base no arquivo
            np.save(arquivo, celulasVazias) # Salva as células vazias no arquivo)
            np.save(arquivo, celulasVazias1d) # Salva as células vazias 1D no arquivo)
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
            numerosValidos = np.load(arquivo) # Lê os números válidos do arquivo
            matrizBase = np.load(arquivo) # Lê a matriz base do arquivo
            celulasVazias = np.load(arquivo) # Lê as células vazias do arquivo
            celulasVazias1d = np.load(arquivo) # Lê as células vazias 1D do arquivo

            parametros.populacao = int.from_bytes(populacao, byteorder='big')
            parametros.geracoes = int.from_bytes(geracoes, byteorder='big')
            parametros.mutacao = int.from_bytes(mutacao, byteorder='big')
            parametros.elitismo = int.from_bytes(elitismo, byteorder='big')
            parametros.torneio = int.from_bytes(torneio, byteorder='big')
            parametros.numerosValidos = numerosValidos
            parametros.matrizBase = matrizBase
            parametros.celulasVazias = celulasVazias
            parametros.celulasVazias1d = celulasVazias1d
    
    except FileNotFoundError as e:
        print(f"Arquivo {e} não foi encontrado.\n")    

    return parametros

'''
    Função fitness:***
        Calcula o fitness de um indivíduo (matriz base mutada ) baseado nas regras do Sudoku.
        
    Parâmetros: 
        matriz - matriz do indivíduo a ser avaliado.
    Retorno:
        Número de caracteres distintos entre a matriz alvo e a matriz cópia.
'''
@njit
def fitness(matriz):
    repetidos = 0

    # Regras básicas do Sudoku:
    # Não pode haver números repetidos em linhas, colunas e submatrizes 3x3
    numLinhas = len(matriz)
    numColunas = len(matriz[0])

    # Verifica repetição de números nas linhas
    for i in range(numLinhas):
        contagemNumerosVistos = np.zeros(10, dtype=np.int8) # 10 pois o índice 0 será ignorado
        for j in range(numColunas):
            numeroAtual = matriz[i,j]
            if numeroAtual != 0:
                contagemNumerosVistos[numeroAtual] += 1
        mascaraRepetidos = contagemNumerosVistos > 1 # Verifica se há números repetidos (True para cada número repetido)
        contagemRepetidos = contagemNumerosVistos[mascaraRepetidos] - 1 # Filtra os números repetidos e subtrai 1 de cada um
        repetidosLinha = np.sum(contagemRepetidos) # Soma os números repetidos de cada linha
        repetidos += repetidosLinha # Adiciona o total de repetidos da linha ao total geral

    # Verifica repetição de números nas colunas
    for i in range(numColunas):
        contagemNumerosVistos = np.zeros(10, dtype=np.int8) 
        for j in range(numLinhas):
            numeroAtual = matriz[j,i]
            if numeroAtual != 0:
                contagemNumerosVistos[numeroAtual] += 1
        mascaraRepetidos = contagemNumerosVistos > 1 # Verifica se há números repetidos (True para cada número repetido)
        contagemRepetidos = contagemNumerosVistos[mascaraRepetidos] - 1 # Filtra os números repetidos e subtrai 1 de cada um
        repetidosColuna = np.sum(contagemRepetidos) # Soma os números repetidos de cada coluna
        repetidos += repetidosColuna # Adiciona o total de repetidos da coluna ao total geral

    # Verifica repetição de números nas submatrizes 3x3
    passo = 3 # Tamanho da submatriz 3x3
    tamanhoMatriz = len(matriz) # Tamanho da matriz (9x9)
    for i in range(0, tamanhoMatriz, passo):
        for j in range(0, tamanhoMatriz, passo):
            submatriz = matriz[i : i + passo, j : j + passo] # Extrai a submatriz 3x3
            contagemNumerosVistos = np.zeros(10, dtype=np.int8)
            for numeroAtual in submatriz.flatten():
                if numeroAtual != 0:
                    contagemNumerosVistos[numeroAtual] += 1
            mascaraRepetidos = contagemNumerosVistos > 1 # Verifica se há números repetidos (True para cada número repetido)
            contagemRepetidos = contagemNumerosVistos[mascaraRepetidos] - 1 # Filtra os números repetidos e subtrai 1 de cada um
            repetidosSubmatriz = np.sum(contagemRepetidos) # Soma os números repetidos de cada submatriz
            repetidos += repetidosSubmatriz # Adiciona o total de repetidos da submatriz ao total geral

    return repetidos

'''
    Função mutacaoAuxiliar:
        Altera aleatoriamente um gene (número) não fixo da matriz do filho, substituindo-o
        por um valor aleatório correspondente a um dos caracteres presentes no intervalo
        numérico da matriz alvo.
    Parâmetros:
        matriz - matriz do indivíduo a ser avaliado.
        taxaMutacao - taxa de mutação (1 a 100).
        numerosValidos - número de caracteres disponíveis para a mutação.
        celulasVazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz após ser mutada.
'''
@njit
def mutacaoAuxiliar(matriz, taxaMutacao, numerosValidos, celulasVazias1d): #vale a pena achatar matrizBase
    # Matriz auxiliar
    novaMatriz = matriz.flatten().copy()
    
    # Verifica se ocorrerá mutação baseado na taxa
    if np.random.randint(0, 100) < taxaMutacao:
        if len(celulasVazias1d) > 0: # Verifica se há células vazias para mutação
            indiceAleatorio = np.random.randint(len(celulasVazias1d))
            posicao = celulasVazias1d[indiceAleatorio] # Escolhe uma posição aleatória da matriz base original
            novoValor = np.random.choice(numerosValidos) # Escolhe um valor aleatório
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
    matrizMutada = mutacaoAuxiliar(filho.matriz, parametros.mutacao, parametros.numerosValidos, parametros.celulasVazias1d)
    
    individuo.matriz = matrizMutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo

'''
    Função recombinacaoUniformeAuxiliar:
        Combina aleatoriamente os genes da matriz pai e mãe nas células do filho 
        que podem ser recombinadas, ou seja, que não são fixas.
    Parâmetros:
        matrizPai - matriz do pai.
        matrizMae - matriz da mãe.
        matrizBase - matriz base.
        celulasVazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz do filho resultante da combinação entre pai e mãe.
'''
@njit
def recombinacaoUniformeAuxiliar(matrizPai, matrizMae, matrizBase, celulasVazias1d):
    matrizPaiUnidimensional = matrizPai.flatten()
    matrizMaeUnidimensional = matrizMae.flatten()

    filho = matrizBase.flatten().copy() # Cria uma cópia da matriz base como ponto de partida para o filho
    
    for i in celulasVazias1d: # Itera sobre as células vazias
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
def recombinacaoUniforme(pai, mae, parametros):
    filho = INDIVIDUO()

    # Certifica que os pais têm representação de array
    if pai.matriz is None or mae.matriz is None:
        return INDIVIDUO() # Retorna indivíduo vazio

    # Realiza a recombinação da matriz unidimensional do filho
    matrizFilho = recombinacaoUniformeAuxiliar(pai.matriz, mae.matriz, parametros.matrizBase, parametros.celulasVazias1d)
    
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


    for i in range(taxaDeElitismo):
        novaPopulacao[i] = INDIVIDUO(populacao[i].fitness, np.copy(populacao[i].matriz))

    for i in range(taxaDeElitismo, parametros.populacao):
        pai = selecaoPorTorneio(populacao, parametros)
        mae = selecaoPorTorneio(populacao, parametros)
        filho = recombinacaoUniforme(pai, mae, parametros)
        filho = mutacao(filho, parametros)
        filho.fitness = fitness(filho.matriz)

        novaPopulacao[i] = filho
        
        if filho.fitness < melhor.fitness:
            melhor = INDIVIDUO(fitness=filho.fitness, matriz=np.copy(filho.matriz))

    for i in range(parametros.populacao):
        populacao[i] = novaPopulacao[i]

    return melhor

'''
    Função geraMatrizesAleatorias:
        Gera matrizes aleatórias de tamanho definido, utilizando os caracteres disponíveis
        no intervalo numérico e com base na matriz base.
    Parâmetros:
        tamanhoPopulacao - número de matrizes a serem geradas.
        numerosValidos - número de caracteres distintos na matriz alvo.
    Retorno:
        Lista de matrizes aleatórias geradas.
'''
@njit
def geraMatrizesAleatorias(tamanhoPopulacao, numerosValidos, matrizBase, celulasVazias):
    
    # Caso os números válidos sejam uma lista vazia ou caso não haja células vazias, retorna um lista de matrizes base
    if len(numerosValidos) == 0 or len(celulasVazias) == 0:
        return [matrizBase.copy() for _ in range(tamanhoPopulacao)]

    matrizes = []

    for _ in range(tamanhoPopulacao):
        matriz = matrizBase.copy()

        for l, c in celulasVazias:
            matriz[l, c] = np.random.choice(numerosValidos)
                
        matrizes.append(matriz)
    
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
    matrizBase = parametros.matrizBase
    celulasVazias = parametros.celulasVazias
    
    matrizesGeradas = geraMatrizesAleatorias(tamanhoPopulacao, intervaloNumeros, matrizBase, celulasVazias)
    
    for i in range(tamanhoPopulacao):
        populacao[i] = INDIVIDUO()
        populacao[i].matriz = matrizesGeradas[i]
        populacao[i].fitness = fitness(populacao[i].matriz)

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