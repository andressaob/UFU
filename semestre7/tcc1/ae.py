import struct
import time
import random
from numba import njit

TAMANHO = 800 # Não alterar
 
class INDIVIDUO:
    def __init__(self, fitness = 0, frase = ""): #__init__ é um método construtor que inicializa os atributos dos objetos
        self.fitness = fitness # Número de caracteres distintos entre a frase alvo e a frase cópia (quanto menor melhor)
        self.frase = frase # Frase cópia

class PARAMETROS:
    def __init__(self, fraseAlvo = "", alfabeto = "", quantidadeLetras = 0, populacao = 0, geracoes = 0, elitismo = 0, mutacao = 0, torneio = 0):
        self.fraseAlvo = fraseAlvo # Frase alvo
        self.alfabeto = alfabeto # Caracteres distintos presentes na frase alvo
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
    populacao = 900
    geracoes = 1800
    mutacao = 15
    elitismo = 5
    torneio = 3
    fraseAlvo = "O Tejo e mais belo que o rio que corre pela minha aldeia,Mas o Tejo nao e mais belo que o rio que corre pela minha aldeia.Porque o Tejo nao e o rio que corre pela minha aldeia,O Tejo tem grandes navios,E nele navega ainda,Para aqueles que veem em tudo o que la nao esta,A memoria das naus.O Tejo desce de Espanha,E o Tejo entra no mar em Portugal.Toda a gente sabe isso.Mas poucos sabem qual e o rio da minha aldeia,E para onde ele vai,E donde ele vem.E por isso, porque pertence a menos gente,e mais livre e maior o rio da minha aldeia.Pelo Tejo vai se para o Mundo.Para alem do Tejo ha a America.E a fortuna daqueles que a encontram.Ninguem nunca pensou no que ha para alem.Do rio da minha aldeia.O rio da minha aldeia nao faz pensar em nada.Quem esta ao pe dele esta so ao pe dele."
    
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
    Função fitnessAuxiliar:
        Calcula o fitness de um indivíduo baseado no número de caracteres distintos 
        entre a frase alvo e a frase cópia. Quanto menor o número de caracteres 
        distintos, melhor o fitness. IMPORTANTE: usa tipos "simples" para evitar 
        problemas com a biblioteca numba, que está auxiliando na otimização.
    Parâmetros: 
        fraseCopia - indivíduo a ser avaliado.
        fraseAlvo - frase alvo.
    Retorno:
        Número de caracteres distintos entre a frase alvo e a frase cópia.
'''
@njit
def fitnessAuxiliar(fraseCopia, fraseAlvo):
    quantidadeDistintos = 0
    tamanhoCopia = len(fraseCopia)
    
    for i in range(len(fraseAlvo)):
        if i < tamanhoCopia and fraseCopia[i] != fraseAlvo[i]:
            quantidadeDistintos += 1
        elif i >= tamanhoCopia:
            quantidadeDistintos += 1
            
    return quantidadeDistintos

'''
    Função fitness:
        Utiliza a função fitnessAuxiliar para calcular o fitness de um indivíduo.
    Parâmetros:
        copia - um dos indivíduos da população.
        parametros - classe PARAMETROS.
    Retorno:
        Retorna o número de caracteres distintos entre a frase alvo e a frase cópia.
'''
def fitness(copia, parametros):
    return fitnessAuxiliar(copia.frase, parametros.fraseAlvo)

'''
    Função mutacaoAuxiliar:
        Altera aleatoriamente um gene (caractere) da frase fornecida (filho), com os 
        genes da frase alvo. IMPORTANTE: usa tipos "simples" para evitar 
        problemas com a biblioteca numba, que está auxiliando na otimização.
    Parâmetros:
        frase - frase a ser mutada.
        taxaMutacao - taxa de mutação (1 a 100).
        tamanhoFraseAlvo - tamanho da frase alvo.
        alfabeto - caracteres distintos na frase alvo.
        tamanhoAlfabeto - número de caracteres disponíveis para a mutação.
    Retorno:
        Frase após ser mutada.
'''
@njit
def mutacaoAuxiliar(frase, taxaMutacao, tamanhoFraseAlvo, alfabeto, tamanhoAlfabeto):
    # Frase auxiliar
    novaFrase = frase
    aleatorio = random.randint(0, 99)
    
    # Verifica se ocorrerá mutação baseado na taxa
    if aleatorio <= taxaMutacao and tamanhoAlfabeto > 0:
        posicao = random.randint(0, tamanhoFraseAlvo - 1)
        # Converte a string em uma lista de caracteres para modificação
        listaFrase = list(novaFrase)
        if posicao < len(novaFrase):
            # Substitui o caractere na posição por um caractere aleatório do alfabeto
            indiceAleatorio = random.randint(0, tamanhoAlfabeto - 1)
            listaFrase[posicao] = alfabeto[indiceAleatorio]
            novaFrase = "".join(listaFrase)
        else:
            # Adiciona um caractere aleatório à frase
            indiceAleatorio = random.randint(0, tamanhoAlfabeto - 1)
            novaFrase += alfabeto[indiceAleatorio]
    
    return novaFrase

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
    individuo = INDIVIDUO(filho.fitness, filho.frase)

    individuo.frase = mutacaoAuxiliar(filho.frase, parametros.mutacao, len(parametros.fraseAlvo), 
                        parametros.alfabeto, parametros.quantidadeLetras)

    return individuo

'''
    Função recombinacaoUniformeAuxiliar:
        Combina aleatoriamente os genes da frase pai e mãe no filho. IMPORTANTE: usa tipos 
        "simples" para evitar problemas com a biblioteca numba, que está auxiliando na otimização.
    Parâmetros:
        frasePai - frase do pai.
        fraseMae - frase da mãe.
        tamanho - tamanho da frase alvo.
    Retorno:
        Frase do filho resultante da combinação entre pai e mãe.
'''
@njit
def recombinacaoUniformeAuxiliar(frasePai, fraseMae, tamanho):
    filhoFrase = ""
    comprimentoMax = min(len(frasePai), len(fraseMae), tamanho)
    
    for i in range(comprimentoMax):
        if random.random() < 0.5:
            filhoFrase += frasePai[i]
        else:
            filhoFrase += fraseMae[i]
            
    return filhoFrase

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
def recombinacaoUniforme(pai, mae, numero):
    filho = INDIVIDUO()
    filho.frase = recombinacaoUniformeAuxiliar(pai.frase, mae.frase, numero)

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
        auxiliar = populacao[random.randint(0, parametros.populacao - 1)]
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
        novaPopulacao[i] = INDIVIDUO(populacao[i].fitness, populacao[i].frase)

    for i in range(taxaDeElitismo, parametros.populacao):
        pai = selecaoPorTorneio(populacao, parametros)
        mae = selecaoPorTorneio(populacao, parametros)
        filho = recombinacaoUniforme(pai, mae, len(parametros.fraseAlvo))
        filho = mutacao(filho, parametros)
        filho.fitness = fitness(filho, parametros)

        if filho.fitness < melhor.fitness:
            melhor = filho
        novaPopulacao[i] = filho

    for i in range(taxaDeElitismo, parametros.populacao):
        populacao[i] = novaPopulacao[i]

    return melhor

'''
    Função geraFrasesAleatorias:
        Gera frases aleatórias de tamanho definido, utilizando os caracteres disponíveis
        no alfabeto. IMPORTANTE: usa tipos "simples" para evitar problemas com a 
        biblioteca numba, que está auxiliando na otimização.
    Parâmetros:
        tamanhoPopulacao - número de frases a serem geradas.
        tamanhoFrase - tamanho de cada frase.
        alfabeto - caracteres distintos na frase alvo.
    Retorno:
        Lista de frases aleatórias geradas.
'''
@njit
def geraFrasesAleatorias(tamanhoPopulacao, tamanhoFrase, alfabeto):
    frases = []
    for i in range(tamanhoPopulacao):
        frase = ""
        for j in range(tamanhoFrase):
            indice = random.randint(0, len(alfabeto) - 1)
            frase += alfabeto[indice]
        frases.append(frase)
    return frases

'''
    Função inicializa:
        Utiliza a função geraFrasesAleatorias para inicializar a população com frases 
        aleatórias de tamanho definido e calcula o fitness de cada uma delas.
    Parâmetros:
        populacao - população de indivíduos (frases cópias).
        parametros - classe PARAMETROS.
    Retorno:
        Nulo.
'''
def inicializa(populacao, parametros):
    alfabeto = parametros.alfabeto
    tamanhoPopulacao = parametros.populacao
    tamanhoFrase = len(parametros.fraseAlvo)
    
    frases_geradas = geraFrasesAleatorias(tamanhoPopulacao, tamanhoFrase, alfabeto)
    
    for i in range(tamanhoPopulacao):
        populacao[i] = INDIVIDUO()
        populacao[i].frase = frases_geradas[i]
        populacao[i].fitness = fitness(populacao[i], parametros)
        
'''
    Função alfabeto:
        Determina quais caracteres compõem a frase alvo.
    Parâmetros:
        parametros - classe PARAMETROS.
    Retorno:
        Retorna a classe PARAMETROS com o alfabeto e a quantidade de letras.
'''
def alfabeto(parametros):
    alfabeto = "".join(sorted(set(parametros.fraseAlvo)))
    
    parametros.alfabeto = alfabeto
    parametros.quantidadeLetras = len(alfabeto)

    return parametros

'''
    Função main:
        Implementa o Algoritmo Evolutivo para o problema: dada uma frase alvo,
        reproduza-a através de uma população de frases cópias geradas aleatoriamente.
'''
def main():
    
    inicio = time.time()

    escreveArquivo()
    parametros = leArquivo()
    parametros = alfabeto(parametros)

    geracao = 0
    populacao = [INDIVIDUO() for _ in range(parametros.populacao)]

    random.seed(time.time_ns())
    inicializa(populacao, parametros)

    while geracao <= parametros.geracoes:
        melhor = reproducao(populacao, parametros)
        print(f"\nIteracao {geracao}, melhor fitness {melhor.fitness}.\n")
        print(f"{melhor.frase}\n")
        geracao += 1
        if melhor.fitness == 0:
            break

    fim = time.time()
    total = fim - inicio
    print(f"Tempo total gasto pela CPU: {total}")
    escreveRelatorio(total, melhor.fitness)

if __name__ == "__main__":
    main()
    #tempo total gasto pela CPU: 147.349347114563, iteração 1091