#importando spacy
import spacy

#importando sys
import sys

def main():
    #"salvando" o nome do arquivo passado como argumento (nesse caso, o 'segundo' porque o 'primeiro' (argv[0])
    #é o arquivo .py)
    baseDocs = sys.argv[1]

    try:
        #carregando o modelo de língua portuguesa do spacy
        nlp = spacy.load('pt_core_news_lg')

        #inicializando o número dos documentos/músicas
        ndocumento = 0

        #criando um dicionário vazio
        M = {}

        #utilizando a estrutura with para abrir e ler o arquivo base_samba.txt (essa estrutura fecha o arquivo automaticamente, 
        #diminuindo a chance de dar problema na manipulação do arquivo)
        with open(baseDocs, encoding='utf8') as base:
            #iterando sobre as linhas de base.txt
            for linha in base:
                #removendo qualquer espaço em branco adicional
                musica = linha.strip()
                ndocumento += 1 #contando a quantidade de documentos/músicas em base.txt
                #abrindo e lendo os arquivos da base de docs, no meu caso, músicas
                with open(musica, encoding='utf8') as f:
                    #armazenando o conteúdo lido
                    conteudo = f.read()
                    #colocando os textos das músicas em uma string
                    #texto += conteudo
                    #colocando o "número" do arquivo e o texto dele em um dicionário
                    elemento = {ndocumento:conteudo}
                    M.update(elemento)

        #criando um novo dicionário vazio
        dIndice = {}

        #dicionário freqs para armazenar a frequência dos termos em cada documento
        freqs = {}

        #percorrendo os valores do dicionário M (docs)
        for c, v in M.items():
            #usa o modelo para analisar o texto, tira as stopwords, pontuações, converte para minúsculo e faz a lematização dos
            #termos
            lemasDoc = [token.lemma_.lower() for token in nlp(v) if token.is_stop == False and token.is_punct == False and token.lemma_.strip() and ' ' not in token.lemma_]
            #se tiver \n na lematização, exclui ele de lemasDoc
            if '\n' in lemasDoc:
                lemasDoc.remove('\n')
            #percorrendo as palavras lematizadas dos textos
            for lema in lemasDoc:
                #lema = lema.strip()
                #inicializando o dicionário freqs com uma palavra (caso já exista no dicionário, mantém o seu valor 
                #atual e caso não exista, um novo dicionário vazio é inicializado)
                freqs[lema] = freqs.get(lema, {})
                #verificando se o doc já está no dicionário de frequências
                if c in freqs[lema]:
                    #se já estiver, incrementa a contagem da frequência no documento atual
                    freqs[lema][c] += 1
                else:
                    #se não, inicia a contagemm da frequência no documento atual
                    freqs[lema][c] = 1
                #atualizando o dicionário do índice invertido com o dicionário freqs
                dIndice[lema] = freqs[lema]

        #ordenando os elementos de dIndice pela chave
        dIndice = dict(sorted(dIndice.items()))

        #gerando o arquivo indice.txt
        #abrindo/criando o arquivo para escrita
        with open('indice.txt', 'w', encoding='utf-8') as file:
            #perecorrendo o dicionário dIndice
            for lema, freqsDoc in dIndice.items():
                #escrevendo o lema no arquivo
                file.write(f'{lema}: ')
                #percorrendo as frequências por documento
                for nDoc, freq in freqsDoc.items():
                    #escrever o "número" do documento e sua frequência no arquivo
                    file.write(f'{nDoc},{freq} ')
                #adicionando uma quebra de linha para os termos ficarem em linhas separadas
                file.write('\n')    

    except FileNotFoundError:
        print(f"O arquivo '{baseDocs}' ou algum arquivo contido nele não foi encontrado.")

if __name__ == "__main__":
    main()
