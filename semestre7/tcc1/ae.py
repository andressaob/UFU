import struct
import time
from numba import njit # Incompatível com classes, sendo necessário a utilização de funções auxiliares para algumas funções
import numpy as np

TAMANHO = 800 # Não alterar

class INDIVIDUO:
    def __init__(self, fitness = 0, fraseArray = None): #__init__ é um método construtor que inicializa os atributos dos objetos
        self.fitness = fitness # Número de caracteres distintos entre a frase alvo e a frase cópia (quanto menor melhor)
        self.fraseArray = fraseArray # Frase cópia representada como array numérico

class PARAMETROS:
    def __init__(self, fraseAlvo = "", quantidadeLetras = 0, populacao = 0, geracoes = 0, elitismo = 0, mutacao = 0, torneio = 0):
        self.fraseAlvo = fraseAlvo # Frase alvo
        self.fraseAlvoArray = None # Frase alvo representada como array numérico
        self.charToInt = {} # Mapeamento char -> int
        self.intToChar = np.array([]) # Mapeamento int -> char (array NumPy)
        self.quantidadeLetras = quantidadeLetras # Número de caracteres distintos presentes na frase alvo
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
    
    fraseAlvo = "O Tejo e mais belo que o rio que corre pela minha aldeia,Mas o Tejo nao e mais belo que o rio que corre pela minha aldeia.Porque o Tejo nao e o rio que corre pela minha aldeia,O Tejo tem grandes navios,E nele navega ainda,Para aqueles que veem em tudo o que la nao esta,A memoria das naus.O Tejo desce de Espanha,E o Tejo entra no mar em Portugal.Toda a gente sabe isso.Mas poucos sabem qual e o rio da minha aldeia,E para onde ele vai,E donde ele vem.E por isso, porque pertence a menos gente,e mais livre e maior o rio da minha aldeia.Pelo Tejo vai se para o Mundo.Para alem do Tejo ha a America.E a fortuna daqueles que a encontram.Ninguem nunca pensou no que ha para alem.Do rio da minha aldeia.O rio da minha aldeia nao faz pensar em nada.Quem esta ao pe dele esta so ao pe dele." #784

    # Trecho adaptado da música "De Volta Para o Futuro" de Fabio Brazza
    #fraseAlvo = "Eram la pelos anos tres mil e o mundo era mais ou menos aquilo que Nostradamus previu.O ser humano frio,num andar robotico,um olhar vazio,um mundo caotico.Eu vi a manipulacao genetica definir antes de nascer,o nosso ser e nossa estetica.Humanidade cetica,desafiando a etica,como se nao passassemos de uma mera formula aritmetica.Vi cidades sendo engolidas pelos mares com o desaparecimento das calotas polares.Eu vi cameras ate no ceu,o verdadeiro Big Brother,como descrito por George Orwel.Seguimos a natureza fria da profecia maquiavelica e a maior industria do mundo continuava sendo a belica." #596

    # Trecho do livro "Em Algum Lugar Nas Estrelas" de Clare Vanderpool
    #fraseAlvo = "A grande ursa negra,impressionante como a Ursa Maior,balancou a cabeca de um lado para o outro,e seu rugido fez tremer a paisagem proxima da Trilha Apalache.Eu digo que e ela,mas a verdade e que nao dava para ter certeza.Nao haviam marcas que inidicavam que era femea.Nao havia filhotes a vista.Mas eu sabia.Eu a conhecia como conhecia minha propria mae.Era sua vontade inabalavel de nos manter vivos." #401

    # Trecho da música "Jesus Chorou" de Racionais MC's
    #fraseAlvo = "O que e, o que e?Clara e salgada,cabe em um olho e pesa uma tonelada.Tem sabor de mar,pode ser discreta.Inquilina da dor,morada predileta.Na calada ela vem,refem da vinganca,irma do desespero,rival da esperança." #211

    try:
        # Gera o arquivo entrada.in para escrita
        with open('entrada.in', 'wb') as arquivo:
            arquivo.write(populacao.to_bytes(4, byteorder='big')) 
            arquivo.write(geracoes.to_bytes(4, byteorder='big'))
            arquivo.write(mutacao.to_bytes(4, byteorder='big'))
            arquivo.write(elitismo.to_bytes(4, byteorder='big'))
            arquivo.write(torneio.to_bytes(4, byteorder='big'))
            arquivo.write(fraseAlvo.encode()) #converte a string para bytes
        # Estrutura with fecha o arquivo automaticamente
    except Exception as e: #caso haja erro na criação do arquivo metricas.in
        print(f"Problemas na criação do arquivo {e}\n")

'''
    Função escreveRelatorio:
        Escreve no arquivo relatorio.txt o tempo de execução do programa e o fitness 
        do melhor indivíduo obtido.
    Parâmetros: 
        tempo - tempo gasto na execução do programa.
        fitness - número de caracteres distintos da frase alvo do indivíduo mais adaptado da População.
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
#função para ler o arquivo entrada.in
def leArquivo():
    try:
        parametros = PARAMETROS()
        # Lê o arquivo entrada.in
        with open('entrada.in', 'rb') as arquivo:
            populacao = arquivo.read(4) #deixar só arquivo.read(4)
            geracoes = arquivo.read(4)
            mutacao = arquivo.read(4)
            elitismo = arquivo.read(4)
            torneio = arquivo.read(4)
            fraseAlvo = arquivo.read(TAMANHO).decode('utf-8').rstrip('\x00')

            parametros.populacao = int.from_bytes(populacao, byteorder='big')
            parametros.geracoes = int.from_bytes(geracoes, byteorder='big')
            parametros.mutacao = int.from_bytes(mutacao, byteorder='big')
            parametros.elitismo = int.from_bytes(elitismo, byteorder='big')
            parametros.torneio = int.from_bytes(torneio, byteorder='big')
            parametros.fraseAlvo = fraseAlvo
    
    except FileNotFoundError as e:
        print(f"Arquivo {e} não foi encontrado.\n")    

    return parametros

'''
    Função fitness:
        Calcula o fitness de um indivíduo baseado no número de caracteres distintos entre 
        a frase alvo e a frase cópia. Quanto menor o número de caracteres distintos, melhor 
        o fitness. Ambas as frases estão representadas como arrays numéricos para melhor 
        compatibilidade com a biblioteca numba, usada para otimizar o código.
    Parâmetros: 
        fraseArray - frase representada como array numérico do indivíduo a ser avaliado.
        fraseAlvoAray - frase alvo representada como array numérico.
    Retorno:
        Número de caracteres distintos entre a frase alvo e a frase cópia.
'''
@njit
def fitness(fraseArray, fraseAlvoAray):
    quantidadeDistintos = 0
    tamanhoCopia = len(fraseArray)
    tamanhoAlvo = len(fraseAlvoAray)

    tamanhoMin = min(tamanhoCopia, tamanhoAlvo)
    for i in range(tamanhoMin):
        if fraseArray[i] != fraseAlvoAray[i]:
            quantidadeDistintos += 1

    # Penalidade pela diferença de tamanho
    quantidadeDistintos += abs(tamanhoCopia - tamanhoAlvo)

    return quantidadeDistintos

'''
    Função mutacaoAuxiliar:
        Altera aleatoriamente um gene (número) da frase do filho, substituindo-o
        por um valor aleatório correspondente a um dos caracteres presentes no alfabeto
        da frase alvo. Ambas as frases estão representadas como arrays numéricos para 
        melhor compatibilidade com a biblioteca numba, usada para otimizar o código.
    Parâmetros:
        fraseArray - frase representada como array numérico do indivíduo a ser avaliado.
        taxaMutacao - taxa de mutação (1 a 100).
        tamanhoFraseAlvo - tamanho da frase alvo.
        tamanhoAlfabeto - número de caracteres disponíveis para a mutação.
    Retorno:
        Frase após ser mutada.
'''
@njit
def mutacaoAuxiliar(fraseArray, taxaMutacao, tamanhoAlfabeto):
    # Frase auxiliar
    novaFraseArray = fraseArray.copy()
    
    # Verifica se ocorrerá mutação baseado na taxa
    if np.random.randint(0, 100) <= taxaMutacao and tamanhoAlfabeto > 0:
        posicao = np.random.randint(len(novaFraseArray))
        novoValor = np.random.randint(0, tamanhoAlfabeto)
        novaFraseArray[posicao] = novoValor
        
    return novaFraseArray

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
    individuo = INDIVIDUO(filho.fitness, filho.fraseArray)

    # Certifica que temos a representação de array
    if filho.fraseArray is None:
        return INDIVIDUO(filho.fitness, None) # Retorna cópia sem array se original não tem

    # Aplica mutação na representação numérica
    individuo.fraseArray = mutacaoAuxiliar(filho.fraseArray, parametros.mutacao, parametros.quantidadeLetras)

    return individuo

'''
    Função recombinacaoUniformeAuxiliar:
        Combina aleatoriamente os genes da frase pai e mãe no filho. Ambas as frases
        estão representadas como arrays numéricos para melhor compatibilidade com a 
        biblioteca numba, usada para otimizar o código.
    Parâmetros:
        frasePaiArray - frase do pai representada como array numérico.
        fraseMaeArray - frase da mãe representada como array numérico.
        tamanho - tamanho da frase alvo.
    Retorno:
        Frase do filho resultante da combinação entre pai e mãe (representada como array numérico).
'''
@njit
def recombinacaoUniformeAuxiliar(frasePaiArray, fraseMaeArray, tamanho):
    comprimentoMax = min(len(frasePaiArray), len(fraseMaeArray), tamanho)
    filhoArray = np.empty(comprimentoMax, dtype=frasePaiArray.dtype)
    
    for i in range(comprimentoMax):
        if np.random.randint(0, 2) == 1:
            filhoArray[i] = frasePaiArray[i]
        else:
            filhoArray[i] = fraseMaeArray[i]
            
    return filhoArray                                                                                                                                               

'''
    Função recombinacaoUniforme:
        Utiliza a função recombinacaoUniformeAuxiliar para realizar a recombinação entre pai e mãe.
    Parâmetros:
        pai - um dos indivíduos da população.
        mae - um dos indivíduos da população.
        numero - tamanho da frase alvo.
    Retorno:
        Indivíduo filho resultante da combinação entre pai e mãe.
'''
def recombinacaoUniforme(pai, mae, numero, parametros):
    filho = INDIVIDUO()

    # Certifica que os pais têm representação de array
    if pai.fraseArray is None or mae.fraseArray is None:
        return INDIVIDUO() # Retorna indivíduo vazio

    filho.fraseArray = recombinacaoUniformeAuxiliar(pai.fraseArray, mae.fraseArray, numero)

    return filho

'''
    Função selecaoPorTorneio:
        Seleciona dois a dois indivíduos da população e determina qual deles possui o menor fitness.
    Parâmetros:
        populacao - população de indivíduos (frases cópias).
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
        população - população de indivíduos (frases cópias).
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
        populacao - população de indivíduos (frases cópias).
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

    melhor = populacao[0]

    for i in range(taxaDeElitismo):
        novaPopulacao[i] = INDIVIDUO(populacao[i].fitness, np.copy(populacao[i].fraseArray))

    for i in range(taxaDeElitismo, parametros.populacao):
        pai = selecaoPorTorneio(populacao, parametros)
        mae = selecaoPorTorneio(populacao, parametros)
        filho = recombinacaoUniforme(pai, mae, len(parametros.fraseAlvoArray), parametros)
        filho = mutacao(filho, parametros)
        filho.fitness = fitness(filho.fraseArray, parametros.fraseAlvoArray)

        if filho.fitness < melhor.fitness:
            melhor = filho
        novaPopulacao[i] = filho

    for i in range(taxaDeElitismo, parametros.populacao):
        populacao[i] = novaPopulacao[i]

    return melhor

'''
    Função geraFrasesAleatorias:
        Gera frases aleatórias de tamanho definido, utilizando os caracteres disponíveis
        no alfabeto. As frases geradas são representadas como arrays numéricos para 
        melhor compatibilidade com a biblioteca numba, usada para otimizar o código.
    Parâmetros:
        tamanhoPopulacao - número de frases a serem geradas.
        tamanhoFrase - tamanho de cada frase (representada em array numérico).
        numLetras - número de caracteres distintos na frase alvo.
    Retorno:
        Lista de frases aleatórias geradas.
'''
@njit
def geraFrasesAleatorias(tamanhoPopulacao, tamanhoFrase, numLetras):
    frases = [np.empty(tamanhoFrase, dtype=np.int64) for _ in range(tamanhoPopulacao)]
    for i in range(tamanhoPopulacao):
        frases[i] = np.random.randint(0, numLetras, size=tamanhoFrase)

    return frases

'''
    Função inicializa:
        Utiliza a função geraFrasesAleatorias para inicializar a população com frases 
        aleatórias (representadas como arrays numéricos) de tamanho definido e 
        calcula o fitness de cada uma delas.
    Parâmetros:
        populacao - população de indivíduos (frases cópias).
        parametros - classe PARAMETROS.
    Retorno:
        Nulo.
'''

def inicializa(populacao, parametros):
    numLetras = parametros.quantidadeLetras
    tamanhoFrase = len(parametros.fraseAlvo)
    tamanhoPopulacao = parametros.populacao
    
    frasesGeradas = geraFrasesAleatorias(tamanhoPopulacao, tamanhoFrase, numLetras)
    
    for i in range(tamanhoPopulacao):
        populacao[i] = INDIVIDUO()
        populacao[i].fraseArray = frasesGeradas[i]
        populacao[i].fitness = fitness(populacao[i].fraseArray, parametros.fraseAlvoArray)
        
'''
    Função alfabeto:
        Determina quais caracteres compõem a frase alvo.
    Parâmetros:
        parametros - classe PARAMETROS.
    Retorno:
        Retorna a classe PARAMETROS com a quantidade de letras, mapeamento 
        entre char <-> int e frase alvo convertida em array numérico.
'''
def alfabeto(parametros):
    alfabeto = "".join(sorted(set(parametros.fraseAlvo)))
    
    parametros.quantidadeLetras = len(alfabeto)

    # Cria mapeamentos char <-> int
    parametros.charToInt = {char: i for i, char in enumerate(alfabeto)}
    parametros.intToChar = np.array(list(alfabeto), dtype=str) # Array para mapeamento reverso rápido

    # Converter fraseAlvo para array numérico (mantendo a string original)
    parametros.fraseAlvoArray = np.array([parametros.charToInt[c] for c in parametros.fraseAlvo], dtype=np.int32)
    

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
    parametros = alfabeto(parametros)

    #print(f"{len(parametros.fraseAlvo)}\n")

    geracao = 0
    populacao = [INDIVIDUO() for _ in range(parametros.populacao)]

    np.random.seed(int(time.time())) # Semente de acordo com o tempo de máquina
    inicializa(populacao, parametros)

    while geracao <= parametros.geracoes:
        melhor = reproducao(populacao, parametros)
        print(f"\nIteracao {geracao}, melhor fitness {melhor.fitness}.\n")
        # Converte a frase do melhor indivíduo para string
        melhorFrase = "".join(parametros.intToChar[melhor.fraseArray]) if melhor.fraseArray is not None else "N/A"
        print(f"{melhorFrase}\n")
        geracao += 1
        if melhor.fitness == 0:
            break

    fim = time.time()
    total = fim - inicio
    print(f"Tempo total gasto pela CPU: {total}")
    escreveRelatorio(total, melhor.fitness)

if __name__ == "__main__":
    main()
