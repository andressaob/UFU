import spacy
import sys
import numpy as np

def main():
    #"salvando" o nome do arquivo passado como argumento
    baseDocs = sys.argv[1]
    #"salvando" a consulta
    consulta = sys.argv[2]

    try:
        #carregando o modelo de língua portuguesa do spacy
        nlp = spacy.load('pt_core_news_lg') 
        conteudoDocs = ''
        #inicializando o "número" dos docs
        ndocumento = 0

        M = {}

        '''
        ABRINDO E LENDO O ARQUIVO DA BASE DE DOCS COM A ESTRUTURA WITH
        '''
        nomeDoc = []
        with open(baseDocs, encoding='utf8') as base:
            #iterando sobre as linhas da base
            for linha in base:
                #removendo qualquer espaço em branco adicional
                doc = linha.strip()
                ndocumento += 1 #contando a quantidade de docs na base
                nomeDoc.append(doc) #salvando os nomes dos docs
                #abrindo e lendo os arquivos da base de docs
                with open(doc, encoding='utf8') as f:
                    #armazenando o conteúdo lido
                    conteudo = f.read()
                    #colocando o "número" do arquivo e o texto dele em um dicionário
                    elemento = {ndocumento:conteudo}
                    M.update(elemento)
                    conteudoDocs += conteudo

        freqs = {} #armazena a frequência dos termos em cada documento
        dIndice = {}

        '''
        CRIAÇÃO E MANIPULAÇÃO DO ÍNDICE INVERTIDO
        '''

        for c, v in M.items():
            #usa o modelo para analisar o texto, tira as stopwords, pontuações, converte para minúsculo e faz a lematização dos
            #termos
            lemasDoc = [token.lemma_.lower() for token in nlp(v) if token.is_stop == False 
                and token.is_punct == False and token.lemma_.strip() and ' ' not in token.lemma_]
            #se tiver \n na lematização, exclui ele de lemasDoc
            if '\n' in lemasDoc:
                lemasDoc.remove('\n')

            for lema in lemasDoc:
                '''inicializando o dicionário freqs com uma palavra (caso já exista no dicionário, mantém o seu  
                   valor atual e caso não exista, um novo dicionário vazio é inicializado)'''
                freqs[lema] = freqs.get(lema, {})
                #verificando se o doc já está em freqs
                if c in freqs[lema]:
                    #se já estiver, incrementa a contagem da frequência no documento atual
                    freqs[lema][c] += 1
                else:
                    #se não, inicia a contagem da frequência no documento atual
                    freqs[lema][c] = 1
                #atualizando o dicionário do índice invertido com o dicionário freqs
                dIndice[lema] = freqs[lema]

        #ordenando os elementos de dIndice pela chave
        dIndice = dict(sorted(dIndice.items()))

        #gerando o arquivo indice.txt:
        with open('indice.txt', 'w', encoding='utf-8') as file:
            #percorrendo o dicionário dIndice
            for lema, freqsDoc in dIndice.items():
                #escrevendo o lema no arquivo
                file.write(f'{lema}: ')
                #percorrendo as frequências por documento
                for nDoc, freq in freqsDoc.items():
                    #escrevendo o "número" do documento e sua frequência no arquivo
                    file.write(f'{nDoc},{freq} ')
                #adicionando uma quebra de linha para os termos ficarem em linhas separadas
                file.write('\n')

        '''
        CALCULANDO TF, IDF e E TF-IDF DOS TERMOS DA BASE DE DOCS
        '''

        #separando os termos do arquivo e colocando eles em uma lista
        termosDocs = [c for c, v in freqs.items()]
        #ordenando essa palhaçada depois de ficar HORAS tentando calcular a similaridade e não dar certo pq os termos não batiam :’(
        termosDocs = sorted(termosDocs)

        #dicionário auxiliar da idfBase, com os termos da base de doc inicializados
        idfAuxBase = {termo: 0 for termo in termosDocs}

        for c, v in idfAuxBase.items():
            if c in freqs:
                '''se o termo estiver em freqs, então o ele "recebe" a quantidade de valores do termo em freqs,
                   que nesse caso representa em quantos docs o termo está presente'''
                idfAuxBase[c] = len(freqs[c])

        #dicionário idfBase para agora sim calcular o idf de cada termo da base
        idfBase = {termo:np.log10(ndocumento/idfAuxBase[termo]) for termo in idfAuxBase}

        #dicionário auxiliar da tfBase, com os termos da base inicializados
        tfAuxBase = {termo: 0 for termo in termosDocs}

        for c, v in freqs.items():
            for termo in tfAuxBase:
                #tfAuxBase recebe a frequência de cada termo da base
                tfAuxBase[termo] = freqs[termo]

        #dicionario tfBase para agora sim calcular o tf de cada termo
        tfBase = {termo: 0 for termo in tfAuxBase}
       
        for termo, vtf in tfBase.items():
            for c, valorTfAux in tfAuxBase.items():
                tfBase[termo] = {c:1 + np.log10(valor) for c, valor in tfAuxBase[termo].items()}
                        
        tfIdfBase = {}

        for c, v in M.items():
            calculaTfIdfBase = {}
            for t in termosDocs:
                #se o doc estiver entre os docs que contém o termo
                if c in [d for d in freqs[t].keys()]:
                    #o cálculo da tf-idf é feito para o termo no doc
                    calculaTfIdfBase.update({t: tfBase[t][c] * idfBase[t]})
                    #o cálculo é adicionado no "vetor" de pesos do doc
                    tfIdfBase[c] = calculaTfIdfBase
                else:
                    #se não, o peso do termo no doc recebe 0
                    calculaTfIdfBase.update({t:0})
                    #colocando apenas 0 caso o doc não contenha o termo para diferenciar dos termos cujo tf-idf deu 0.0
                    tfIdfBase[c] = calculaTfIdfBase

        '''
        ABRINDO E LENDO O ARQUIVO CONSULTA
        '''

        with open(consulta, encoding='utf8') as q:
            conteudoConsulta = q.read()

        '''
        CALCULANDO TF E TF-IDF DOS TERMOS DA CONSULTA
        '''

        #separando os termos da consulta, processando e colocando eles em uma lista
        termosConsulta = [t.lemma_.lower() for t in nlp(conteudoConsulta) if t.lemma_ != '&' and t.lemma_.split()]

        #frequência do termo na consulta
        freqsConsulta = {}

        for termo in termosConsulta:
            #inicializando cada termo em freqsConsulta
            freqsConsulta[termo] = freqsConsulta.get(termo, 0)
            #caso tenha termo repetido na consulta:
            if termo in freqsConsulta:    
                freqsConsulta[termo] += 1
            else:
                freqsConsulta[termo] = 1
        
        #dicionário tfConsulta para calcular o tf de cada termo
        tfConsulta = {t:1 + np.log10(v) for c, v in freqsConsulta.items() for t in termosConsulta}

        tfIdfConsulta = {}

        #gambiarra para saber quais são os termos da base que estão ausentes na consulta
        termosAusentesConsulta = list(set(termosDocs).difference(set(termosConsulta)))

        #calculando o tf-idf dos termos da consulta
        for t in termosConsulta:
            tfIdfConsulta.update({t: tfConsulta[t] * idfBase[t]})
        #calculando o tf-idf dos termos que estão ausentes na consulta, pois serão necessários posteriormente
        for t in termosAusentesConsulta:
            #termos que estão ausentes na consulta mas presentes na base
            tfIdfConsulta.update({t:0})

        #ordenando o dicionário tfIdfConsulta
        tfIdfConsulta = dict(sorted(tfIdfConsulta.items()))

        '''
        GERANDO O ARQUIVO PESOS.TXT
        '''

        with open('pesos.txt', 'w', encoding='utf-8') as file:
            #percorrendo o dicionário tfIdfBase
            for doc, v in tfIdfBase.items():
                #escrevendo o nº do doc no arquivo
                file.write(f'{doc}: ')
                #percorrendo a tf-idf de cada termo em cada arquivo
                for t, tfidf in v.items():
                    if tfidf != 0:
                        #escrevendo o termo e a tf-idf dele em cada doc
                        file.write(f'{t}, {tfidf}   ')
                #adicionando uma quebra de linha para os termos ficarem em linhas separadas
                file.write('\n')

        '''
        CALCULANDO A SIMILARIDADE ENTRE DOCS E CONSULTA
        '''
    
        similaridade = {}
        docsRetornados = 0

        for d, v in tfIdfBase.items():
            '''transformando os dicionário em vetores de tf-idf, tomando cuidado para que os índices de ambos correspondam 
               ao mesmo termo'''
            vetorBase = [tfIdfBase[d][t] for t in termosDocs]
            vetorConsulta = [tfIdfConsulta[t] for t in termosDocs]
            '''calculando a similaridade de cada doc com a consulta: método dot calcula o produto escalar dos vetores e método 
               norm retorna a norma do vetor'''
            if (np.linalg.norm(vetorBase)) == 0 or (np.linalg.norm(vetorConsulta)) == 0:
                #verificando se os vetores têm norma 0, para evitar divisão por 0
                similaridade[d] = 0
            else:
                similaridade[d] = np.dot(vetorBase, vetorConsulta) / (np.linalg.norm(vetorBase) * np.linalg.norm(vetorConsulta))
            if similaridade[d] >= 0.001:
                docsRetornados += 1

        #ordenando a similaridade em ordem decrescente        
        similaridade = dict(sorted(similaridade.items(), key=lambda item: item[1], reverse=True))

        '''
        GERANDO O ARQUIVO RESPOSTA.TXT
        '''

        with open('resposta.txt', 'w', encoding='utf-8') as file:
            file.write(f'{docsRetornados}\n')
            #percorrendo o dicionário similaridade
            for d, v in similaridade.items():
                if v >= 0.001:   
                    #escrevendo o nº do doc no arquivo
                    file.write(f'{nomeDoc[d-1]}: {(v)}\n')
    
    except FileNotFoundError:
        print(f"O arquivo '{baseDocs}' ou algum arquivo contido nele não foi encontrado.")

if __name__ == "__main__":
    main()