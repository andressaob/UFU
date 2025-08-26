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
        self.elitismo = elitismo # Taxa de elitismo (0 a 99)
        self.mutacao = mutacao # Taxa de mutação (0 a 99)
        self.torneio = torneio # Número de participantes da seleção por torneio

'''
    Função escreve_arquivo:
        Escreve no arquivo entrada.in a matriz base alvo e os parâmetros especificados.
'''
def escreve_arquivo():
    populacao = 600
    geracoes = 200
    mutacao = 3
    elitismo = 10
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
    passo = 3 # Tamanho da submatriz 3x3
    tamanho_matriz = len(matriz) # Tamanho da matriz (9x9)

    # Verifica repetição de números nas linhas
    for i in range(num_linhas):
        contagem = np.bincount(matriz[i, :]) # Conta a ocorrência de cada número na linha
        repetidos += np.sum(contagem[contagem > 1] - 1) # Soma o número de repetições (ocorrências - 1)
        
    # Verifica repetição de números nas colunas
    for j in range(num_colunas):
        contagem = np.bincount(matriz[:, j]) # Conta a ocorrência de cada número na coluna
        repetidos += np.sum(contagem[contagem > 1] - 1) # Soma o número de repetições (ocorrências - 1)
        
    # Verifica repetição de números nas submatrizes 3x3
    for i in range(0, tamanho_matriz, passo): # Itera sobre as linhas com passo de 3
        for j in range(0, tamanho_matriz, passo): # Itera sobre as colunas com passo de 3
            submatriz = matriz[i:i+passo, j:j+passo].flatten() # Extrai a submatriz 3x3 e a transforma em um array unidimensional
            contagem = np.bincount(submatriz) # Conta a ocorrência de cada número na submatriz
            repetidos += np.sum(contagem[contagem > 1] - 1) # Soma o número de repetições (ocorrências - 1)
            
    return repetidos

'''
    Função mutacao_auxiliar:
        Faz a mutação por Reset Aleatório, que altera aleatoriamente um gene 
        (número) não fixo da matriz do filho, substituindo-o por um valor aleatório
        correspondente a um dos números válidos do Sudoku.
    Parâmetros:
        matriz - matriz do indivíduo a ser avaliado.
        taxa_mutacao - taxa de mutação (1 a 100).
        numeros_validos - caracteres disponíveis para a mutação.
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz após ser mutada.
'''
@njit
def mutacao_auxiliar(matriz, taxa_mutacao, numeros_validos, celulas_vazias1d): # Usada para testes
    # Matriz auxiliar
    nova_matriz = matriz.flatten().copy()
    probabilidade_mutacao = taxa_mutacao/100
    
    # Verifica se ocorrerá mutação baseado na taxa
    if np.random.random() <= probabilidade_mutacao:
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
def mutacao(filho, parametros): # Usada para testes
    individuo = Individuo(filho.fitness, filho.matriz)

    # Certifica que a matriz do filho não é None
    if filho.matriz is None:
        return Individuo(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Realiza a mutação da matriz unidimensional do filho
    matriz_mutada = mutacao_auxiliar(filho.matriz, parametros.mutacao, parametros.numeros_validos, parametros.celulas_vazias1d)
    
    individuo.matriz = matriz_mutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo

'''
    Função mutacao_por_troca_auxiliar:
        Altera o genoma do indivíduo trocando os valores de duas posições
        aleatórias que não são fixas na matriz
    Parâmetros:
        matriz - matriz do indivíduo a ser avaliado.
        taxa_mutacao - taxa de mutação (0 a 99).
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz após ser mutada.
'''
@njit
def mutacao_por_troca_auxiliar(matriz, taxa_mutacao, celulas_vazias1d): # Usada para testes
    nova_matriz = matriz.flatten().copy()

    probabilidade_mutacao = taxa_mutacao/100
    
    # Verifica se ocorrerá mutação baseado na probabilidade
    if np.random.random() < taxa_mutacao:
        # Garante que há pelo menos duas células para trocar
        if len(celulas_vazias1d) >= 2:
            indices_para_troca = np.random.choice(np.arange(len(celulas_vazias1d)), 2, replace=False) # replace=False garante que os índices são únicos
            posicao1 = celulas_vazias1d[indices_para_troca[0]]
            posicao2 = celulas_vazias1d[indices_para_troca[1]]
            # Realiza a troca
            valor_temp = nova_matriz[posicao1]
            nova_matriz[posicao1] = nova_matriz[posicao2]
            nova_matriz[posicao2] = valor_temp
        
    return nova_matriz # Retorna matriz unidimensional mutada ou a original se não ocorreu mutação

'''
    Função mutacao_por_troca:
        Utiliza a função mutacao_por_troca_auxiliar para realizar a mutação de um indivíduo.
    Parâmetros:
        filho - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo mutado.
'''
def mutacao_por_troca(filho, parametros): # Usada para testes
    individuo = Individuo(filho.fitness, filho.matriz)

    # Certifica que a matriz do filho não é None
    if filho.matriz is None:
        return Individuo(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Realiza a mutação da matriz unidimensional do filho
    matriz_mutada = mutacao_por_troca_auxiliar(filho.matriz, parametros.mutacao, parametros.celulas_vazias1d)
    
    individuo.matriz = matriz_mutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo
    
'''
    Função mutacao_por_gene_auxiliar:
        Aplica a mutação em cada célula não fixa da matriz, alterando seu valor com base na
        probabilidade de mutação.
    Parâmetros:
        matriz - matriz do indivíduo a ser mutado.
        taxa_mutacao - taxa de mutação (0 a 100).
        numeros_validos - números válidos para o Sudoku.
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz do indivíduo mutada.
'''
@njit
def mutacao_por_gene_auxiliar(matriz, taxa_mutacao, numeros_validos, celulas_vazias1d):  # Teve o melhor desempenho nos testes
    # Matriz auxiliar
    nova_matriz = matriz.flatten().copy()
    probabilidade_mutacao = taxa_mutacao/100
    
    # Verifica se há células para mutar
    if len(celulas_vazias1d) == 0:
        return nova_matriz

    # Itera sobre CADA célula não-fixa
    for posicao in celulas_vazias1d:
        # Cada célula tem sua própria chance de sofrer mutação
        if np.random.random() <= probabilidade_mutacao:
            # Se a mutação ocorrer para esta célula, escolhe um novo valor
            novoValor = np.random.choice(numeros_validos)
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
def mutacao_por_gene(filho, parametros): # Teve o melhor desempenho nos testes
    individuo = Individuo(filho.fitness, filho.matriz)

    # Certifica que a matriz do filho não é None
    if filho.matriz is None:
        return Individuo(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Realiza a mutação da matriz unidimensional do filho
    matriz_mutada = mutacao_por_gene_auxiliar(filho.matriz, parametros.mutacao, parametros.numeros_validos, parametros.celulas_vazias1d)
    
    individuo.matriz = matriz_mutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo

'''
    Função recombinacao_uniforme_auxiliar:
        Aplica a recombinação uniforme, combinando aleatoriamente os genes (cada célula)
        da matriz pai e mãe nas células do filho que podem ser recombinadas, ou seja, que não são fixas.
    Parâmetros:
        matriz_pai - matriz do pai.
        matriz_mae - matriz da mãe.
        matriz_base - matriz base.
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz do filho resultante da combinação entre pai e mãe.
'''
@njit
def recombinacao_uniforme_auxiliar(matriz_pai, matriz_mae, matriz_base, celulas_vazias1d): # Teve o melhor desempenho nos testes
    matriz_pai_unidimensional = matriz_pai.flatten()
    matriz_mae_unidimensional = matriz_mae.flatten()

    filho = matriz_base.flatten().copy() # Cria uma cópia da matriz base como ponto de partida para o filho
    
    for i in celulas_vazias1d: # Itera sobre as células vazias
        if np.random.randint(0, 2) == 1:
            filho[i] = matriz_pai_unidimensional[i]
        else:
            filho[i] = matriz_mae_unidimensional[i]
            
    return filho # Retorna filho como array unidimensional'''

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
def recombinacao_uniforme(pai, mae, parametros): # Teve o melhor desempenho nos testes
    filho = Individuo()

    # Certifica que os pais têm representação de array
    if pai.matriz is None or mae.matriz is None:
        return Individuo() # Retorna indivíduo vazio

    # Realiza a recombinação da matriz unidimensional do filho
    matriz_filho = recombinacao_uniforme_auxiliar(pai.matriz, mae.matriz, parametros.matriz_base, parametros.celulas_vazias1d)
    
    filho.matriz = matriz_filho.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return filho

'''
    Função recombinacao_ponto_de_corte_auxiliar:
        Combina os genes (valores nas células não fixas) do pai e da mãe utilizando
        a técnica de um ponto de corte - onde o filho herda os genes do pai até o ponto
        de corte e os genes da mãe depois do ponto de corte- e dois pontos de corte - onde
        o filho herda os genes do pai antes do primeiro ponto de corte e depois do segundo
        e os genes da mãe entre o primeiro e segundo pontos de corte.
    Parâmetros:
        matriz_pai - matriz do pai.
        matriz_mae - matriz da mãe.
        matriz_base - matriz base.
        celulas_vazias1d - posições das células vazias na matriz base em formato unidimensional.
    Retorno:
        Matriz unidimensional do filho resultante da combinação entre pai e mãe.
'''

@njit
def recombinacao_ponto_de_corte_auxiliar(matriz_pai, matriz_mae, matriz_base, celulas_vazias1d): # Usada para testes
    # Extrai os genes dos pais
    genes_pai = matriz_pai.flatten()[celulas_vazias1d]
    genes_mae = matriz_mae.flatten()[celulas_vazias1d]

    num_genes = len(celulas_vazias1d)

    # Se não houver genes para trocar (Sudoku completo), retorna uma cópia da matriz base.
    if num_genes == 0:
        return matriz_base.flatten().copy()

    # Se o ponto for 0, o filho é uma cópia da mãe. Se for num_genes, é uma cópia do pai.
    ponto_de_corte = np.random.randint(0, num_genes + 1)

    # ----------------- 2 pontos -----------------
    ponto1 = np.random.randint(0, num_genes)
    ponto2 = np.random.randint(0, num_genes)

    # Garante que os pontos sejam diferentes
    while ponto1 == ponto2:
        ponto2 = np.random.randint(0, num_genes)

    # Ordena os pontos para facilitar a concatenação
    if ponto1 > ponto2:
        ponto1, ponto2 = ponto2, ponto1 # Troca os valores

    # Cria o cromossomo do filho, herdando as "pontas" do pai e o "meio" da mãe.
    genes_filho = np.concatenate((genes_pai[:ponto1], genes_mae[ponto1:ponto2], genes_pai[ponto2:]))
    # ----------------- 2 pontos -----------------

    # Cria o cromossomo do filho (células originalmente vazias)
    genes_filho = np.concatenate((genes_pai[:ponto_de_corte], genes_mae[ponto_de_corte:]))

    filho = matriz_base.flatten().copy() # Começa com a matriz base para o filho
    for i in range(num_genes):
        posicao = celulas_vazias1d[i]
        valor = genes_filho[i]
        filho[posicao] = valor
            
    return filho # Retorna o filho como um array unidimensional

'''
    Função recombinacao_ponto_de_corte:
        Utiliza a função recombinacao_ponto_de_corte_auxiliar para realizar a recombinação
        entre pai e mãe.
    Parâmetros:
        pai - um dos indivíduos da população.
        mae - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo filho resultante da combinação entre pai e mãe.
'''
def recombinacao_ponto_de_corte(pai, mae, parametros): # Usada para testes
    filho = Individuo()

    # Certifica que os pais têm matrizes para recombinar
    if pai.matriz is None or mae.matriz is None:
        return Individuo() # Retorna indivíduo vazio

    # Realiza a recombinação da matriz unidimensional do filho
    matriz_filho = recombinacao_ponto_de_corte_auxiliar(pai.matriz, mae.matriz, parametros.matriz_base, parametros.celulas_vazias1d)
    
    filho.matriz = matriz_filho.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return filho

@njit
def recombinacao_por_bloco_auxiliar(matriz_pai, matriz_mae, matriz_base): # Usada para testes
    filho = matriz_base.copy() # Células fixas do filho são as mesmas da matriz base
    passo = 3 # Tamanho do bloco

    # Itera sobre a grade de blocos 3x3
    for i in range(0, 9, passo):
        for j in range(0, 9, passo):
            # Sorteia de qual pai o bloco será herdado (0 = pai, 1 = mae)
            if np.random.randint(0, 2) == 0:
                # As célulasfixas são sobrescritas com o mesmo valor que já tinham.
                filho[i:i+passo, j:j+passo] = matriz_pai[i:i+passo, j:j+passo]
            else:
                filho[i:i+passo, j:j+passo] = matriz_mae[i:i+passo, j:j+passo]
                
    return filho # Retorna a matriz completa do filho

'''
    Função recombinacao_por_bloco:
        Utiliza a função recombinacao_por_bloco_auxiliar para realizar a recombinação.
    Parâmetros:
        pai - um dos indivíduos da população.
        mae - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo filho resultante da combinação entre pai e mãe.
'''
def recombinacao_por_bloco(pai, mae, parametros): # Usada para testes
    filho = Individuo()

    if pai.matriz is None or mae.matriz is None:
        return Individuo()

    matriz_filho = recombinacao_por_bloco_auxiliar(pai.matriz, mae.matriz, parametros.matriz_base)
    
    filho.matriz = matriz_filho

    return filho

'''
    Função recombinacao_bloco_1_ponto_auxiliar:
        Combina os blocos do pai e da mãe utilizando a técnica de um ponto de corte,
        onde o filho herda os blocos do pai até o ponto de corte e os blocos da mãe 
        depois do ponto de corte.
    Parâmetros:
        matriz_pai - matriz do pai.
        matriz_mae - matriz da mãe.
        matriz_base - matriz base.
    Retorno:
        Matriz do filho resultante da combinação entre pai e mãe.
'''
@njit
def recombinacao_bloco_1_ponto_auxiliar(matriz_pai, matriz_mae, matriz_base): # Usada para testes
    filho = matriz_base.copy()
    passo = 3 # Tamanho do bloco

    # O cromossomo aqui é a sequência de 9 blocos.
    # Se o ponto de corte for 0, todos os blocos vêm da mãe.
    # Se for 9, todos os blocos vêm do pai.
    ponto_de_corte = np.random.randint(1, 9) # Sorteia um número entre 1 e 9

    # Itera sobre os 9 blocos, de 0 a 8
    for indice_bloco in range(9):
        # Calcula a posição (linha, coluna) do canto superior esquerdo do bloco
        linha_inicio = (indice_bloco // 3) * passo
        coluna_inicio = (indice_bloco % 3) * passo
        
        # Decide de qual pai herdar com base no ponto de corte
        if indice_bloco < ponto_de_corte:
            # Herda o bloco do pai
            bloco_para_copiar = matriz_pai[linha_inicio : linha_inicio+passo, coluna_inicio : coluna_inicio+passo]
        else:
            # Herda o bloco da mãe
            bloco_para_copiar = matriz_mae[linha_inicio : linha_inicio+passo, coluna_inicio : coluna_inicio+passo]
        
        # Copia o bloco selecionado para o filho
        filho[linha_inicio : linha_inicio+passo, coluna_inicio : coluna_inicio+passo] = bloco_para_copiar
    
    return filho

'''
    Função recombinacao_bloco_1_ponto:
        Utiliza a função recombinacao_corte_por_bloco_auxiliar para realizar a recombinação
        entre pai e mãe.
    Parâmetros:
        pai - um dos indivíduos da população.
        mae - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo filho resultante da combinação entre pai e mãe.
'''
def recombinacao_bloco_1_ponto(pai, mae, parametros): # Usada para testes
    filho = Individuo()

    if pai.matriz is None or mae.matriz is None:
        return Individuo()

    matriz_filho = recombinacao_bloco_1_ponto_auxiliar(pai.matriz, mae.matriz, parametros.matriz_base)
    
    filho.matriz = matriz_filho

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
def selecao_por_torneio(populacao, parametros): # Teve o melhor desempenho
    melhor = Individuo()
    melhor.fitness = -1

    for i in range(parametros.torneio):
        auxiliar = populacao[np.random.randint(0, parametros.populacao)]
        if melhor.fitness == -1 or auxiliar.fitness < melhor.fitness:
            melhor = auxiliar

    return melhor

'''
    Função selecao_por_roleta:
        Seleciona um indivíduo da população baseado em uma roleta, 
        onde a probabilidade de seleção é inversamente proporcional ao fitness.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
    Retorno:
        Retorna o indivíduo selecionado pela roleta.
'''
def selecao_por_roleta(populacao): # Usada para testes
    # Converte o fitness: um fitness menor (melhor) tem uma fatia maior.
    # Adição de 1.0 para evitar divisão por zero se o fitness for 0.
    aptidoes = [1.0 / (1.0 + individuo.fitness) for individuo in populacao]
    soma_total_aptdao = sum(aptidoes)

    # Se a soma for zero, retorna um aleatório.
    if soma_total_aptdao == 0:
        return populacao[np.random.randint(0, len(populacao))]
    
    probabilidades = [aptidao/soma_total_aptdao for aptidao in aptidoes]

    # "Gira" a roleta gerando um ponto aleatório.
    ponto_aleatorio = np.random.random()

    # Encontra o indivíduo correspondente ao ponto da roleta.
    soma_parcial = 0
    for i, prob in enumerate(probabilidades):
        soma_parcial += prob
        if soma_parcial >= ponto_aleatorio:
            return populacao[i]

    # Caso de imprecisão aritmética, retorna o último indivíduo.        
    return populacao[-1]

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
        #pai = selecao_por_roleta(populacao)
        #mae = selecao_por_roleta(populacao)
        filho = recombinacao_uniforme(pai, mae, parametros)
        #filho = recombinacao_ponto_de_corte(pai, mae, parametros)
        #filho = recombinacao_por_bloco(pai, mae, parametros)
        #filho = recombinacao_bloco_1_ponto(pai, mae, parametros)
        #filho = mutacao(filho, parametros)
        #filho = mutacao_por_troca(filho, parametros)
        filho = mutacao_por_gene(filho, parametros)
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
    Função gera_matrizes_aleatorias:
        Função alternativa que implementa a inicialização em que os números da subgrade não são repetidos.
    Parâmetros:
        numeros_validos - número de caracteres distintos na matriz alvo.
    Retorno:
        Lista de matrizes aleatórias geradas.
'''
@njit
def gera_matrizes_aleatorias(tamanho_populacao, numeros_validos, matriz_base, celulas_vazias):
    matrizes = []
    passo = 3 # Define o tamanho da submatriz (3x3)
    tamanho_matriz = len(matriz_base) # Tamanho da matriz (9x9)


    for _ in range(tamanho_populacao):
        # Começa com uma cópia nova da matriz base para cada indivíduo
        matriz_individuo = matriz_base.copy()
        # Itera sobre cada bloco 3x3 da matriz
        for i in range(0, tamanho_matriz, passo):
            for j in range(0, tamanho_matriz, passo):
                # Extrai a submatriz atual
                submatriz = matriz_individuo[i:i+passo, j:j+passo]
                # Encontra os números que já estão fixos no bloco
                numeros_presentes = set()
                for valor in submatriz.flatten():
                    if valor != 0:
                        numeros_presentes.add(valor)
                # Determina quais números estão faltando para preencher o bloco
                numeros_faltantes = []
                for numero in numeros_validos:
                    if numero not in numeros_presentes:
                        numeros_faltantes.append(numero)
                # Embaralha aleatoriamente os números que faltam
                np.random.shuffle(np.array(numeros_faltantes))
                # Preenche as células vazias do bloco com os números embaralhados
                indice_faltante = 0
                for l in range(passo):
                    for c in range(passo):
                        if matriz_individuo[i+l, j+c] == 0:
                            matriz_individuo[i+l, j+c] = numeros_faltantes[indice_faltante]
                            indice_faltante += 1
                            
        matrizes.append(matriz_individuo)
        
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

    try:
        # Gravando o tempo de execução real
        with open('tempoExec.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(f'{total}')
    except Exception as e: # Caso haja erro na criação do arquivo tempoExec.txt
        print(f"Problemas na criação do arquivo {e}\n")

    print(f"Tempo total gasto pela CPU: {total}")

if __name__ == "__main__":
    main()
