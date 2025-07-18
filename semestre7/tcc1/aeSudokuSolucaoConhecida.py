import time
from numba import njit # Incompatível com classes, sendo necessário a utilização de funções auxiliares para algumas funções
import numpy as np
import struct 

class Individuo:
    #__init__ é um método construtor que inicializa os atributos dos objetos
    def __init__(self, fitness = 0, matriz = None):
        self.fitness = fitness # Número de caracteres repetidos em cada linha, coluna ou submatriz
        self.matriz = matriz # Matriz contendo as nove 'submatrizes'

class Parametros:
    def __init__(self, numeros_validos = None, matriz_base = None, celulas_vazias = None, celulas_vazias1d = None, 
                populacao = 0, geracoes = 0, elitismo = 0, mutacao = 0, torneio = 0):
        self.numeros_validos = numeros_validos # Números válidos (1-9) para o Sudoku
        self.matriz_base = matriz_base # Matriz base
        self.celulas_vazias = celulas_vazias # Posições das células vazias na matriz base
        self.celulas_vazias1d = celulas_vazias1d # Posições das células vazias na matriz base em formato unidimensional
        self.populacao = populacao # Tamanho da população
        self.geracoes = geracoes # Número de gerações
        self.elitismo = elitismo # Taxa de elitismo (1 a 100)
        self.mutacao = mutacao # Taxa de mutação (1 a 100)
        self.torneio = torneio # Número de participantes da seleção por torneio

'''
    Função escreve_arquivo:
        Escreve no arquivo entrada.in a matriz base alvo e os parâmetros especificados.
'''
def escreve_arquivo():
    populacao = 600
    geracoes = 200
    mutacao = 0.125
    elitismo = 15
    torneio = 3

    matriz_base = np.block([[0,8,4, 0,7,2, 1,0,5], 
                            [2,0,7, 8,3,0, 9,0,0], 
                            [6,0,0, 5,0,9, 0,0,8], 
                            [0,6,0, 9,2,8, 4,0,0],
                            [0,7,0, 0,0,0, 0,6,9], 
                            [0,2,0, 0,0,0, 0,8,1], 
                            [0,3,2, 0,5,0, 6,9,4], 
                            [7,0,0, 0,0,0, 0,0,2], 
                            [1,0,0, 2,0,4, 0,0,7]])
    
    celulas_vazias = np.argwhere(matriz_base == 0) # Posições das células vazias na matriz base
    celulas_vazias1d = np.where(matriz_base.flatten() == 0)[0] # Posições das células vazias na matriz base em formato unidimensional
    numeros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Números válidos para o Sudoku
    
    try:
        # Gera o arquivo entrada.in para escrita
        with open('entrada.in', 'wb') as arquivo:
            arquivo.write(populacao.to_bytes(4, byteorder='big')) 
            arquivo.write(geracoes.to_bytes(4, byteorder='big'))
            #arquivo.write(mutacao.to_bytes(4, byteorder='big'))
            arquivo.write(struct.pack('>f', mutacao))
            arquivo.write(elitismo.to_bytes(4, byteorder='big'))
            arquivo.write(torneio.to_bytes(4, byteorder='big'))
            np.save(arquivo, numeros_validos) # Salva os números válidos no arquivo
            np.save(arquivo, matriz_base) # Salva a matriz base no arquivo
            np.save(arquivo, celulas_vazias) # Salva as células vazias no arquivo)
            np.save(arquivo, celulas_vazias1d) # Salva as células vazias 1D no arquivo)
        # Estrutura with fecha o arquivo automaticamente
    except Exception as e: # Caso haja erro na criação do arquivo metricas.in
        print(f"Problemas na criação do arquivo {e}\n")

'''
    Função escreve_relatorio:
        Escreve no arquivo relatorio.txt a geração e o fitness de cada execução.
    Parâmetros: 
        geracao - número da geração atual.
        fitness - quantidade de números repetidos em linhas, colunas ou submatrizes.
    Retorno:
        Nulo.
'''
def escreve_relatorio(geracao, fitness):
    try:
        modo = 'w' if geracao == 0 else 'a' # Se for a primeira geração, cria o arquivo, se não adiciona ao final
        # Gravando os dados no arquivo relatorio.txt
        with open('relatorio.txt', modo, encoding='utf-8') as arquivo:
            arquivo.write(f'Geracao: {geracao:}, fitness: {fitness:}\n')
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
    Função le_arquivo:
        Lê no arquivo entrada.in com os parâmetros definidos pelo usuário
        para os testes.
    Retorno:
        Instância da classe Parametros com os parâmetros lidos.
'''
def le_arquivo():
    try:
        parametros = Parametros()
        # Lê o arquivo entrada.in
        with open('entrada.in', 'rb') as arquivo:
            populacao = arquivo.read(4) 
            geracoes = arquivo.read(4)
            mutacao = arquivo.read(4)
            elitismo = arquivo.read(4)
            torneio = arquivo.read(4)
            numeros_validos = np.load(arquivo) # Lê os números válidos do arquivo
            matriz_base = np.load(arquivo) # Lê a matriz base do arquivo
            celulas_vazias = np.load(arquivo) # Lê as células vazias do arquivo
            celulas_vazias1d = np.load(arquivo) # Lê as células vazias 1D do arquivo

            parametros.populacao = int.from_bytes(populacao, byteorder='big')
            parametros.geracoes = int.from_bytes(geracoes, byteorder='big')
            #parametros.mutacao = int.from_bytes(mutacao, byteorder='big')
            parametros.mutacao = struct.unpack('>f', mutacao)[0]
            parametros.elitismo = int.from_bytes(elitismo, byteorder='big')
            parametros.torneio = int.from_bytes(torneio, byteorder='big')
            parametros.numeros_validos = numeros_validos
            parametros.matriz_base = matriz_base
            parametros.celulas_vazias = celulas_vazias
            parametros.celulas_vazias1d = celulas_vazias1d
    
    except FileNotFoundError as e:
        print(f"Arquivo {e} não foi encontrado.\n")    

    return parametros

'''
    Função fitness:
        Calcula o fitness de um indivíduo (matriz base mutada) baseado nas regras do Sudoku.
    Parâmetros: 
        matriz - matriz do indivíduo a ser avaliado.
    Retorno:
        Quantidade de números repetidos em linhas, colunas e submatrizes.
'''
@njit
def fitness(matriz):
    repetidos = 0

    # Regras básicas do Sudoku:
    # Não pode haver números repetidos em linhas, colunas e submatrizes 3x3
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Verifica repetição de números nas linhas
    for i in range(num_linhas):
        contagem_numeros_vistos = np.zeros(10, dtype=np.int8) # 10 pois o índice 0 será ignorado
        for j in range(num_colunas):
            numero_atual = matriz[i,j]
            if numero_atual != 0:
                contagem_numeros_vistos[numero_atual] += 1
        mascara_repetidos = contagem_numeros_vistos > 1 # Verifica se há números repetidos (True para cada número repetido)
        contagem_repetidos = contagem_numeros_vistos[mascara_repetidos] - 1 # Filtra os números repetidos e subtrai 1 de cada um
        repetidos_linha = np.sum(contagem_repetidos) # Soma os números repetidos de cada linha
        repetidos += repetidos_linha # Adiciona o total de repetidos da linha ao total geral

    # Verifica repetição de números nas colunas
    for i in range(num_colunas):
        contagem_numeros_vistos = np.zeros(10, dtype=np.int8) 
        for j in range(num_linhas):
            numero_atual = matriz[j,i]
            if numero_atual != 0:
                contagem_numeros_vistos[numero_atual] += 1
        mascara_repetidos = contagem_numeros_vistos > 1 # Verifica se há números repetidos (True para cada número repetido)
        contagem_repetidos = contagem_numeros_vistos[mascara_repetidos] - 1 # Filtra os números repetidos e subtrai 1 de cada um
        repetidos_coluna = np.sum(contagem_repetidos) # Soma os números repetidos de cada coluna
        repetidos += repetidos_coluna # Adiciona o total de repetidos da coluna ao total geral

    # Verifica repetição de números nas submatrizes 3x3
    passo = 3 # Tamanho da submatriz 3x3
    tamanho_matriz = len(matriz) # Tamanho da matriz (9x9)
    for i in range(0, tamanho_matriz, passo):
        for j in range(0, tamanho_matriz, passo):
            submatriz = matriz[i : i + passo, j : j + passo] # Extrai a submatriz 3x3
            contagem_numeros_vistos = np.zeros(10, dtype=np.int8)
            for numero_atual in submatriz.flatten():
                if numero_atual != 0:
                    contagem_numeros_vistos[numero_atual] += 1
            mascara_repetidos = contagem_numeros_vistos > 1 # Verifica se há números repetidos (True para cada número repetido)
            contagem_repetidos = contagem_numeros_vistos[mascara_repetidos] - 1 # Filtra os números repetidos e subtrai 1 de cada um
            repetidos_submatriz = np.sum(contagem_repetidos) # Soma os números repetidos de cada submatriz
            repetidos += repetidos_submatriz # Adiciona o total de repetidos da submatriz ao total geral

    return repetidos

'''
    Função mutacao_auxiliar:
        Altera aleatoriamente um gene (número) não fixo da matriz do filho, substituindo-o
        por um valor aleatório correspondente a um dos números válidos do Sudoku.
    Parâmetros:
        matriz - matriz do indivíduo a ser avaliado.
        taxa_mutacao - taxa de mutação (1 a 100).
        numeros_validos - caracteres disponíveis para a mutação.
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz após ser mutada.
'''
@njit
def mutacao_auxiliar(matriz, taxa_mutacao, numeros_validos, celulas_vazias1d):
    # Matriz auxiliar
    nova_matriz = matriz.flatten().copy()
    
    # Verifica se ocorrerá mutação baseado na taxa
    if np.random.randint(0, 100) < taxa_mutacao:
        if len(celulas_vazias1d) > 0: # Verifica se há células vazias para mutação
            indiceAleatorio = np.random.randint(len(celulas_vazias1d))
            posicao = celulas_vazias1d[indiceAleatorio] # Escolhe uma posição aleatória da matriz base original
            novoValor = np.random.choice(numeros_validos) # Escolhe um valor aleatório
            nova_matriz[posicao] = novoValor
        
    return nova_matriz # Retorna matriz unidimensional mutada

'''
    Função mutacao:
        Utiliza a função mutacao_auxiliar para realizar a mutação de um indivíduo.
    Parâmetros:
        filho - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo mutado.
'''
def mutacao(filho, parametros):
    individuo = Individuo(filho.fitness, filho.matriz)

    # Certifica que a matriz do filho não é None
    if filho.matriz is None:
        return Individuo(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Realiza a mutação da matriz unidimensional do filho
    matriz_mutada = mutacao_auxiliar(filho.matriz, parametros.mutacao, parametros.numeros_validos, parametros.celulas_vazias1d)
    
    individuo.matriz = matriz_mutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo

'''
    Função recombinacao_uniforme_auxiliar:
        Combina aleatoriamente os genes da matriz pai e mãe nas células do filho 
        que podem ser recombinadas, ou seja, que não são fixas.
    Parâmetros:
        matriz_pai - matriz do pai.
        matriz_mae - matriz da mãe.
        matriz_base - matriz base.
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz do filho resultante da combinação entre pai e mãe.
'''
@njit
def recombinacao_uniforme_auxiliar(matriz_pai, matriz_mae, matriz_base, celulas_vazias1d):
    matriz_pai_unidimensional = matriz_pai.flatten()
    matriz_mae_unidimensional = matriz_mae.flatten()

    filho = matriz_base.flatten().copy() # Cria uma cópia da matriz base como ponto de partida para o filho
    
    for i in celulas_vazias1d: # Itera sobre as células vazias
        if np.random.randint(0, 2) == 1:
            filho[i] = matriz_pai_unidimensional[i]
        else:
            filho[i] = matriz_mae_unidimensional[i]
            
    return filho # Retorna filho como array unidimensional                                                                                                                                          

'''
    Função recombinacao_uniforme:
        Utiliza a função recombinacao_uniforme_auxiliar para realizar a recombinação entre pai e mãe.
    Parâmetros:
        pai - um dos indivíduos da população.
        mae - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo filho resultante da combinação entre pai e mãe.
'''
def recombinacao_uniforme(pai, mae, parametros):
    filho = Individuo()

    # Certifica que os pais têm representação de array
    if pai.matriz is None or mae.matriz is None:
        return Individuo() # Retorna indivíduo vazio

    # Realiza a recombinação da matriz unidimensional do filho
    matriz_filho = recombinacao_uniforme_auxiliar(pai.matriz, mae.matriz, parametros.matriz_base, parametros.celulas_vazias1d)
    
    filho.matriz = matriz_filho.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return filho

'''
    Função selecao_por_torneio:
        Seleciona dois a dois indivíduos da população e determina qual deles possui o menor fitness.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
        parametros - classe Parametros.
    Retorno:
        Retorna o indivíduo com o menor fitness entre os selecionados.
'''
def selecao_por_torneio(populacao, parametros):
    melhor = Individuo()
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
        parametros - classe Parametros.
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
        parametros - classe Parametros.
    Retorno:
        Retorna o melhor indivíduo da população.
'''
def reproducao(populacao, parametros):
    melhor = Individuo()
    pai = Individuo()
    mae = Individuo()
    filho = Individuo()
    nova_populacao = [Individuo() for _ in range(parametros.populacao)]

    taxa_de_elitismo = elitismo(populacao, parametros)

    melhor = Individuo(fitness=populacao[0].fitness, matriz=np.copy(populacao[0].matriz))


    for i in range(taxa_de_elitismo):
        nova_populacao[i] = Individuo(populacao[i].fitness, np.copy(populacao[i].matriz))

    for i in range(taxa_de_elitismo, parametros.populacao):
        pai = selecao_por_torneio(populacao, parametros)
        mae = selecao_por_torneio(populacao, parametros)
        filho = recombinacao_uniforme(pai, mae, parametros)
        filho = mutacao(filho, parametros)
        filho.fitness = fitness(filho.matriz)

        nova_populacao[i] = filho
        
        if filho.fitness < melhor.fitness:
            melhor = Individuo(fitness=filho.fitness, matriz=np.copy(filho.matriz))

    for i in range(parametros.populacao):
        populacao[i] = nova_populacao[i]

    return melhor

'''
    Função gera_matrizes_aleatorias:
        Gera matrizes aleatórias de tamanho definido, utilizando os caracteres disponíveis
        no intervalo numérico e com base na matriz base.
    Parâmetros:
        tamanho_populacao - número de matrizes a serem geradas.
        numeros_validos - número de caracteres distintos na matriz alvo.
    Retorno:
        Lista de matrizes aleatórias geradas.
'''
@njit
def gera_matrizes_aleatorias(tamanho_populacao, numeros_validos, matriz_base, celulas_vazias):
    
    # Caso os números válidos sejam uma lista vazia ou caso não haja células vazias, retorna um lista de matrizes base
    if len(numeros_validos) == 0 or len(celulas_vazias) == 0:
        return [matriz_base.copy() for _ in range(tamanho_populacao)]

    matrizes = []

    for _ in range(tamanho_populacao):
        matriz = matriz_base.copy()

        for l, c in celulas_vazias:
            matriz[l, c] = np.random.choice(numeros_validos)
                
        matrizes.append(matriz)
    
    return matrizes

'''
    Função inicializa:
        Utiliza a função gera_matrizes_aleatorias para inicializar a população com matrizes 
        aleatórias de tamanho definido e calcula o fitness de cada uma delas.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
        parametros - classe Parametros.
    Retorno:
        Nulo.
'''

def inicializa(populacao, parametros):
    intervalo_numeros = parametros.numeros_validos
    tamanho_populacao = parametros.populacao
    matriz_base = parametros.matriz_base
    celulas_vazias = parametros.celulas_vazias
    
    matrizes_geradas = gera_matrizes_aleatorias(tamanho_populacao, intervalo_numeros, matriz_base, celulas_vazias)
    
    for i in range(tamanho_populacao):
        populacao[i] = Individuo()
        populacao[i].matriz = matrizes_geradas[i]
        populacao[i].fitness = fitness(populacao[i].matriz)

'''
    Função set_seed: 
        Define uma semente para o gerador de números aleatórios usado pela biblioteca
        numba, permitindo reprodutibilidade nos testes.
    Parâmetros:
        seed - semente a ser definida.
    Retorno:
        Nulo.
'''
'''@njit
def set_seed(seed):
    np.random.seed(seed)'''

'''
    Função main:
        Implementa o Algoritmo Evolutivo para o problema: dada uma instância do jogo Sudoku (matriz base),
        ache a solução através de uma população de matrizes cópias preenchidas aleatoriamente.
'''

def main():
    #np.random.seed(0) # Semente fixa para testes
    #setSeed(0) # Semente fixa para testes
    
    inicio = time.time()

    escreve_arquivo()
    parametros = le_arquivo()

    geracao = 0
    populacao = [Individuo() for _ in range(parametros.populacao)]

    np.random.seed(int(time.time())) # Semente de acordo com o tempo de máquina
    inicializa(populacao, parametros)
    while geracao <= parametros.geracoes:
        melhor = reproducao(populacao, parametros)
        print(f"\nIteracao {geracao}, melhor fitness {melhor.fitness}.\n")
        escreve_relatorio(geracao, melhor.fitness)
        print(f"{melhor.matriz}\n")
        geracao += 1
        if melhor.fitness == 0:
            break

    fim = time.time()
    total = fim - inicio
    print(f"Tempo total gasto pela CPU: {total}")

if __name__ == "__main__":
    main()
