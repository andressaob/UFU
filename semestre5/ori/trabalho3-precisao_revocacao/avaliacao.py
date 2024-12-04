import matplotlib.pyplot as plt
import sys

def main():
    referencia = sys.argv[1]

    try:
        linhas = {}
        respostasIdeais = {}
        respostasSistema = {}
        nLinha = 0

        with open(referencia, encoding='utf8') as arquivo:
            #número de consultas de referência
            nConsultasRef = int(arquivo.readline())
            #lendo as linhas do arquivo
            for linha in arquivo:
                nLinha += 1
                elementoL = {nLinha:linha.split()}
                linhas.update(elementoL)
                #dicionário linhas tem todas as linhas do arquivo, menos a primeira (que é o número de consultas de referência)
        
        #dicionário com as respostas ideais
        for consulta, resposta in linhas.items():
            '''entra no dicionário respostasIdeais apenas as linhas correspondentes às respostas ideais (primeira metade das 
            linhas do dicionário linhas)'''
            if consulta <= (nLinha - nConsultasRef):
                elementoI = {consulta:resposta}
                respostasIdeais.update(elementoI)

        #dicionário com as respostas do sistema
        for consulta, resposta in linhas.items():
            '''entra no dicionário respostasSistema apenas as linhas correspondentes às respostas do sistema (segunda metade 
            das linhas do dicionário linhas)'''
            if consulta > (nLinha - nConsultasRef):
                elementoI = {consulta-nConsultasRef:resposta}
                respostasSistema.update(elementoI)        

        #dicionário de precisão e revocação de todas as consultas
        precisaoRevocacaoOriginal = {}
        
        for consulta, resposta in respostasSistema.items():
            #dicionário auxiliar de precisão e revocação de cada consulta
            precisaoRevocacao = {}
            nDocReleante = 0
            for i in resposta:
                if i in respostasIdeais[consulta]:
                    nDocReleante += 1
                    '''precisao = "índice" do doc relevante (primeiro doc relevante recuperado, segundo ...) / "índice" 
                    do doc em respostasSistema'''
                    precisao = nDocReleante / (respostasSistema[consulta].index(i)+1)
                    revocacao = nDocReleante / len(respostasIdeais[consulta])
                    elemento = {revocacao:precisao}
                    precisaoRevocacao.update(elemento)
            precisaoRevocacaoOriginal.update({consulta:precisaoRevocacao})
        
        #colocando os 11 níveis de revocação no dicionário niveisPrecisaoRevocacao
        niveisPrecisaoRevocacao = {}
        for consulta, precisaorevocacao in precisaoRevocacaoOriginal.items():
            elemento = {consulta:{0.0:None, 0.1:None, 0.2:None, 0.3:None, 0.4:None, 0.5:None, 0.6:None, 0.7:None, 0.8:None, 
                        0.9:None, 1.0:None}}
            niveisPrecisaoRevocacao.update(elemento)

        #fazendo a interpolação
        for consulta, precisaorevocacao in niveisPrecisaoRevocacao.items():
            for revocacao in precisaorevocacao.keys():
                maximo = 0
                for auxp in precisaoRevocacaoOriginal[consulta]:
                    if auxp >= revocacao:
                        if maximo < precisaoRevocacaoOriginal[consulta][auxp]:
                            maximo = precisaoRevocacaoOriginal[consulta][auxp]
                precisaorevocacao[revocacao] = maximo 

        #plotando os gráficos das consultas
        for consulta, precisaorevocacao in niveisPrecisaoRevocacao.items():
            plt.figure()
            plt.plot(list(precisaorevocacao.keys()), list(precisaorevocacao.values()), 'b')#plota o gráfico para cada consulta
            plt.xlabel('Revocação')
            plt.ylabel('Precisão')
            plt.title(f'Consulta {consulta}')
            plt.show()
        
        #calculando a média do sistema
        media = {}
        for consulta, precisaorevocacao in niveisPrecisaoRevocacao.items():
            for revocacao, precisao in precisaorevocacao.items():
                if revocacao not in media:
                    media[revocacao] = 0
                media[revocacao] += precisao / nConsultasRef

        #plotando o gráfico da média
        plt.figure()
        plt.plot(list(media.keys()), list(media.values()), 'b') #plota o gráfico para cada consulta
        plt.xlabel('Revocação')
        plt.ylabel('Precisão')
        plt.title(f'Média')
        plt.show()

        #gerando o arquivo media.txt
        with open('media.txt', 'w', encoding='utf-8') as file:
            for c, v in media.items():
                file.write(f'{media[c]}  ')
              
    except FileNotFoundError:
        print(f"O arquivo '{referencia}' não foi encontrado.")

if __name__ == "__main__":
    main()
