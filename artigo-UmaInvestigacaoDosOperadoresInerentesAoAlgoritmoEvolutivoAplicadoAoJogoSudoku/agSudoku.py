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
    def __init__(self, numeros_validos = None, matriz_base = None, populacao = 0, geracoes = 0, elitismo = 0, mutacao = 0, torneio = 0):
        self.numeros_validos = numeros_validos # Números válidos (1-9) para o Sudoku
        self.matriz_base = matriz_base # Matriz base
        #self.celulas_vazias = celulas_vazias # Posições das células vazias na matriz base
        #self.celulas_vazias1d = celulas_vazias1d # Posições das células vazias na matriz base em formato unidimensional
        self.populacao = populacao # Tamanho da população
        self.geracoes = geracoes # Número de gerações
        self.elitismo = elitismo # Taxa de elitismo (0 a 99)
        self.mutacao = mutacao # Taxa de mutação (0 a 99)
        self.torneio = torneio # Número de participantes da seleção por torneio

'''
    Função escreve_arquivo:
        Escreve no arquivo entradaArtigo.in a matriz base alvo e os parâmetros especificados.
'''
def escreve_arquivo():
    populacao = 600
    geracoes = 200
    mutacao = 5.0
    elitismo = 5
    torneio = 3

    # 0 representa células vazias na matriz base
    matriz_base = np.array([[0,8,4, 0,7,2, 1,0,5], 
                            [2,0,7, 8,3,0, 9,0,0], 
                            [6,0,0, 5,0,9, 0,0,8], 
                            [0,6,0, 9,2,8, 4,0,0],
                            [0,7,0, 0,0,0, 0,6,9], 
                            [0,2,0, 0,0,0, 0,8,1], 
                            [0,3,2, 0,5,0, 6,9,4], 
                            [7,0,0, 0,0,0, 0,0,2], 
                            [1,0,0, 2,0,4, 0,0,7]])
    
    numeros_validos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # Números válidos para o Sudoku
    
    try:
        # Gera o arquivo entradaArtigo.in para escrita
        with open('entradaArtigo.in', 'wb') as arquivo:
            arquivo.write(populacao.to_bytes(4, byteorder='big')) 
            arquivo.write(geracoes.to_bytes(4, byteorder='big'))
            arquivo.write(struct.pack('>f', mutacao))
            arquivo.write(elitismo.to_bytes(4, byteorder='big'))
            arquivo.write(torneio.to_bytes(4, byteorder='big'))
            np.save(arquivo, numeros_validos) # Salva os números válidos no arquivo
            np.save(arquivo, matriz_base) # Salva a matriz base no arquivo
        # Estrutura with fecha o arquivo automaticamente
    except Exception as e: # Caso haja erro na criação do arquivo entradaArtigo.in
        print(f"Problemas na criação do arquivo {e}\n")

'''
    Função escreve_relatorio:
        Registra no arquivo 'relatorioArtigo.txt' o histórico de evolução (geração e fitness).
    Parâmetros: 
        historico_fitness - lista de tuplas (geração, fitness).
    Retorno:
        Nulo.
'''
def escreve_relatorio(historico_fitness):
    try:
        # Gravando os dados no arquivo relatorioArtigo.txt
        with open('relatorioArtigo.txt', 'w', encoding='utf-8') as arquivo:
            for geracao, fitness in historico_fitness:
                arquivo.write(f'Geracao: {geracao:}, fitness: {fitness:}\n')
    except Exception as e: # Caso haja erro na criação do arquivo relatorioArtigo.txt
        print(f"Problemas na criação do arquivo {e}\n")

'''
    Função le_arquivo:
        Lê no arquivo entradaArtigo.in com os parâmetros definidos pelo usuário.
    Retorno:
        Instância da classe Parametros com os parâmetros lidos.
'''
def le_arquivo():
    try:
        parametros = Parametros()
        # Lê o arquivo entradaArtigo.in
        with open('entradaArtigo.in', 'rb') as arquivo:
            populacao = arquivo.read(4) 
            geracoes = arquivo.read(4)
            mutacao = arquivo.read(4)
            elitismo = arquivo.read(4)
            torneio = arquivo.read(4)
            numeros_validos = np.load(arquivo)
            matriz_base = np.load(arquivo)

            parametros.populacao = int.from_bytes(populacao, byteorder='big')
            parametros.geracoes = int.from_bytes(geracoes, byteorder='big')
            parametros.mutacao = struct.unpack('>f', mutacao)[0]
            parametros.elitismo = int.from_bytes(elitismo, byteorder='big')
            parametros.torneio = int.from_bytes(torneio, byteorder='big')
            parametros.numeros_validos = numeros_validos
            parametros.matriz_base = matriz_base
    
    except FileNotFoundError as e:
        print(f"Arquivo {e} não foi encontrado.\n")    

    return parametros

'''
    Função fitness:
        Calcula o fitness de um indivíduo.
        NOTA: Como a inicialização e os operadores garantem que cada LINHA contenha
        os números de 1 a 9 sem repetição, não é necessário verificar repetições nas linhas.
    Parâmetros: 
        matriz - matriz do indivíduo a ser avaliado.
    Retorno:
        Quantidade de números repetidos em colunas e submatrizes 3x3.
'''
@njit
def fitness(matriz):
    repetidos = 0
    num_colunas = len(matriz[0])
    passo = 3 # Tamanho da submatriz 3x3
    tamanho_matriz = len(matriz) # Tamanho da matriz (9x9)

    # Regras básicas do Sudoku:
    # Não pode haver números repetidos em linhas, colunas e submatrizes 3x3
        
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
    Função mutacao_por_troca_auxiliar:
        Percorre cada linha e, com base na taxa de mutação, troca dois valores
        que não sejam fixos (da matriz base original).
    Parâmetros:
        matriz - matriz do indivíduo a ser avaliado.
        taxa_mutacao - taxa de mutação (0 a 99).
        matriz_base - matriz original do problema (para identificar posições fixas).
    Retorno:
        Matriz unidimensional após ser mutada.
'''
@njit
def mutacao_por_troca_auxiliar(matriz, taxa_mutacao, matriz_base):
    nova_matriz = matriz.flatten().copy()
    matriz_base_1d = matriz_base.flatten()

    probabilidade_mutacao = taxa_mutacao/100

    num_linhas = len(matriz_base)

    for i in range(num_linhas):
        # Verifica se ocorrerá mutação baseado na probabilidade
        if np.random.random() < probabilidade_mutacao:
            indice_linha = i

            # Encontra índices de células vazias NESSA LINHA
            inicio_linha = indice_linha * 9
            fim_linha = inicio_linha + 9

            # Índices globais (0-80) das células vazias (originais) nessa linha
            celulas_vazias_linha = []
            for j in range(inicio_linha, fim_linha):
                if matriz_base_1d[j] == 0:
                    celulas_vazias_linha.append(j)

            # Garante que há pelo menos duas células para trocar
            if len(celulas_vazias_linha) >= 2:
                # Seleciona dois índices aleatórios (da lista de vazios)
                indice1 = np.random.randint(0, len(celulas_vazias_linha))
                indice2 = np.random.randint(0, len(celulas_vazias_linha))
                while(indice1 == indice2):
                    indice2 = np.random.randint(0, len(celulas_vazias_linha))

                # Obtém as posições reais (0-80) a partir dos índices da lista
                posicao1 = celulas_vazias_linha[indice1]
                posicao2 = celulas_vazias_linha[indice2]

                # Realiza a troca
                valor_temp = nova_matriz[posicao1]
                nova_matriz[posicao1] = nova_matriz[posicao2]
                nova_matriz[posicao2] = valor_temp
        
    return nova_matriz

'''
    Função mutacao_por_troca:
        Utiliza a função mutacao_por_troca_auxiliar para realizar a mutação de um indivíduo.
    Parâmetros:
        filho - um dos indivíduos da população.
        parametros - classe Parametros.
    Retorno:
        Indivíduo mutado.
'''
def mutacao_por_troca(filho, parametros):
    individuo = Individuo(filho.fitness, filho.matriz)

    # Certifica que a matriz do filho não é None
    if filho.matriz is None:
        return Individuo(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Realiza a mutação da matriz unidimensional do filho
    matriz_mutada = mutacao_por_troca_auxiliar(filho.matriz, parametros.mutacao, parametros.matriz_base)

    individuo.matriz = matriz_mutada.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9

    return individuo

'''
    Função recombinacao_linha_ox_auxiliar:
        Realiza a recombinação OX (Order Crossover) linha a linha entre dois indivíduos pais,
        respeitando os genes fixos da matriz base e a não repetição de números na linha.
    Parâmetros:
        matriz_pai - matriz do indivíduo pai.
        matriz_mae - matriz do indivíduo mãe.
        matriz_base - matriz original do problema (para identificar posições fixas).
    Retorno:
        Matriz unidimensional do indivíduo filho após a recombinação.
'''

@njit
def recombinacao_linha_ox_auxiliar(matriz_pai, matriz_mae, matriz_base): # Usada para testes
    num_linhas = len(matriz_base)
    filho = matriz_base.copy()

    # Arrays de trabalho pré-alocados
    # Usado como um "Set" para marcar genes 1-9 já usados
    genes_usados = np.zeros(num_linhas + 1, dtype=np.bool_) 
    # Lista de genes a serem preenchidos, na ordem da mãe
    lista_mae = np.zeros(num_linhas, dtype=np.int32) 

    for i in range(num_linhas):
        # Obtém referências das linhas
        linha_pai = matriz_pai[i]
        linha_mae = matriz_mae[i]
        linha_base = matriz_base[i]
        linha_filho = filho[i]

        # Reseta arrays de trabalho
        genes_usados[:] = False
        lista_mae[:] = 0

        # Gera pontos de corte aleatórios
        ponto1 = np.random.randint(0, num_linhas)
        ponto2 = np.random.randint(0, num_linhas)
        while ponto1 == ponto2:
            ponto2 = np.random.randint(0, num_linhas)
            
        if ponto1 > ponto2:
            ponto1, ponto2 = ponto2, ponto1 # Garante ponto1 <= ponto2

        # Marca genes fixos E copiar a fatia do pai 
        for j in range(num_linhas):
            gene_fixo = linha_base[j]
            if gene_fixo != 0:
                # Marca o gene fixo (da base) como "usado"
                genes_usados[gene_fixo] = True

        for j in range(ponto1, ponto2):
            if linha_base[j] == 0:
                # Se não é fixo E está na fatia...
                gene_pai = linha_pai[j]
                
                # SÓ atribua E marque se o gene ainda não foi usado
                if not genes_usados[gene_pai]:
                    linha_filho[j] = gene_pai
                    genes_usados[gene_pai] = True
        
        # Coleta, na ordem da mãe, os genes que ainda não foram usados
        count = 0
        for j in range(num_linhas):
            gene_mae = linha_mae[j]
            if not genes_usados[gene_mae]:
                lista_mae[count] = gene_mae
                count += 1
                # Marca como usado para evitar duplicatas (caso a mãe seja inválida)
                genes_usados[gene_mae] = True 

        # Preenche TODOS os "buracos" restantes ---
        indice_lista = 0 # Ponteiro para a lista_mae
        for j in range(num_linhas):
            # Se é um "buraco", preencha.
            if linha_filho[j] == 0:
                linha_filho[j] = lista_mae[indice_lista]
                indice_lista += 1
            
            
    return filho

'''
    Função recombinacao_linha_ox:
        Utiliza a função recombinacao_linha_ox_auxiliar para realizar a recombinação de dois indivíduos pais.
    Parâmetros:
        pai - indivíduo pai.
        mae - indivíduo mãe.
        parametros - classe Parametros.
    Retorno:
        Indivíduo filho resultante da recombinação.
'''
def recombinacao_linha_ox(pai, mae, parametros):
    filho = Individuo()

    # Certifica que os pais têm matrizes para recombinar
    if pai.matriz is None or mae.matriz is None:
        return Individuo() # Retorna indivíduo vazio

    # Realiza a recombinação da matriz unidimensional do filho
    matriz_filho = recombinacao_linha_ox_auxiliar(pai.matriz, mae.matriz, parametros.matriz_base)
    
    #filho.matriz = matriz_filho.reshape((9, 9)) # Transforma o array unidimensional em matriz 9x9
    filho.matriz = matriz_filho

    return filho

'''
    Função selecao_por_torneio:
        Seleciona um indivíduo da população através do método de seleção por torneio.
    Parâmetros:
        populacao - população de indivíduos (matrizes cópias).
        parametros - classe Parametros.
    Retorno:
        Indivíduo selecionado.
'''
def selecao_por_torneio(populacao, parametros): # Teve o melhor desempenho nos testes
    melhor = Individuo()
    melhor.fitness = -1

    for i in range(parametros.torneio):
        auxiliar = populacao[np.random.randint(0, parametros.populacao)]
        if melhor.fitness == -1 or auxiliar.fitness < melhor.fitness:
            melhor = auxiliar

    return melhor

'''
    Função elitismo:
        Ordena a população e calcula quantos indivíduos serão preservados.
    Parâmetros:
        população - população de indivíduos (matrizes cópias).
        parametros - classe Parametros.
    Retorno:
        Número de indivíduos selecionados.
'''
def elitismo(populacao, parametros):
    selecionados = (parametros.populacao * parametros.elitismo) // 100
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
        while mae == pai:
            mae = selecao_por_torneio(populacao, parametros)

        filho = recombinacao_linha_ox(pai, mae, parametros)
        filho = mutacao_por_troca(filho, parametros)
        filho.fitness = fitness(filho.matriz)

        nova_populacao[i] = filho
        
        if filho.fitness < melhor.fitness:
            melhor = Individuo(fitness=filho.fitness, matriz=np.copy(filho.matriz))

    for i in range(parametros.populacao):
        populacao[i] = nova_populacao[i]

    return melhor

'''
    Função gera_matrizes_aleatorias:
        Gera a população inicial. Para cada linha, preenche os zeros com os 
        números que faltam (1-9) embaralhados.
    Parâmetros:
        tamanho_populacao - tamanho da população.
        numeros_validos - números válidos (1-9) para o Sudoku.
        matriz_base - matriz base do Sudoku.
    Retorno:
        Lista de matrizes aleatórias.
'''
@njit
def gera_matrizes_aleatorias(tamanho_populacao, numeros_validos, matriz_base):
    matrizes = []
    tamanho_matriz = len(matriz_base) # Tamanho da matriz (9x9)

    for _ in range(tamanho_populacao):
        # Começa com uma cópia nova da matriz base para cada indivíduo
        matriz_individuo = matriz_base.copy()

        for i in range(tamanho_matriz):
            linha_atual = matriz_individuo[i, :]
            # Encontra os números que já estão na linha (os números-dica)
            numeros_existentes = set(linha_atual[linha_atual != 0])

            # Descobre quais números (1-9) estão faltando
            numeros_faltantes = []
            for numero in numeros_validos:
                if numero not in numeros_existentes:
                    numeros_faltantes.append(numero)
            numeros_faltantes = np.array(numeros_faltantes)

            # Embaralha APENAS os números que faltam
            np.random.shuffle(numeros_faltantes)

            # Encontra os índices (posições) onde a linha é igual a 0
            indices_dos_zeros = np.where(linha_atual == 0)[0]

            # Substitui os zeros pelos números faltantes embaralhados
            if len(indices_dos_zeros) == len(numeros_faltantes):
                matriz_individuo[i, indices_dos_zeros] = numeros_faltantes
                            
        matrizes.append(matriz_individuo.copy())
        
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
    numeros_validos = parametros.numeros_validos
    tamanho_populacao = parametros.populacao
    matriz_base = parametros.matriz_base
    
    matrizes_geradas = gera_matrizes_aleatorias(tamanho_populacao, numeros_validos, matriz_base)
    
    for i in range(parametros.populacao):
        populacao[i] = Individuo()
        populacao[i].matriz = matrizes_geradas[i]
        populacao[i].fitness = fitness(populacao[i].matriz)

'''
    Função main:
        Fluxo principal de execução.
'''

def main():
    inicio = time.time()

    escreve_arquivo()
    parametros = le_arquivo()

    geracao = 0
    populacao = [Individuo() for _ in range(parametros.populacao)]

    historico_fitness = [] # Lista para guardar o histórico

    np.random.seed(int(time.time())) # Semente de acordo com o tempo de máquina
    inicializa(populacao, parametros)
    
    while geracao <= parametros.geracoes:
        melhor = reproducao(populacao, parametros)
        print(f"\nIteracao {geracao}, melhor fitness {melhor.fitness}.\n")
        historico_fitness.append((geracao, melhor.fitness))
        print(f"{melhor.matriz}\n")
        geracao += 1
        if melhor.fitness == 0:
            break

    fim = time.time()
    total = fim - inicio

    escreve_relatorio(historico_fitness)

    try:
        # Gravando o tempo de execução real
        with open('tempoExec.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(f'{total}')
    except Exception as e: # Caso haja erro na criação do arquivo tempoExec.txt
        print(f"Problemas na criação do arquivo {e}\n")

    print(f"Tempo total gasto pela CPU: {total}")

if __name__ == "__main__":
    main()
