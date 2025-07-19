# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys
import re

'''
    Função plotarGrafico:
        Cria e exibe um gráfico de Fitness vs. Geração.
    Parâmetros:
        valores_geracoes (list): Lista de inteiros para o eixo X.
        valores_fitness (list): Lista de inteiros/floats para o eixo Y.
    Retorno:
        Nenhum. Exibe o gráfico diretamente.
'''

def plotar_grafico(valores_geracoes, valores_fitness):
    plt.figure(figsize=(9, 5))

    # Obtém o eixo atual (gca = Get Current Axes) e define a proporção
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    plt.plot(valores_geracoes, valores_fitness, color='b')
    
    plt.xlabel('Geração')
    plt.ylabel('Fitness')
    plt.title('Evolução do Fitness por Geração')
    plt.grid(True)
    
    # Ajusta os eixos para mostrar melhor a tendência
    if valores_geracoes:
        # Arredonda o valor máximo para a próxima dezena
        max_x = (max(valores_geracoes) // 10) * 10
        plt.xticks(range(0, max_x + 1, 10)) # Define os marcadores do eixo X
        plt.xlim(left=0)

    if valores_fitness:
        # Arredonda o valor máximo para a próxima dezena
        max_y = int((max(valores_fitness) // 10) * 10)
        plt.yticks(range(0, max_y + 1, 10)) # Define os marcadores do eixo Y    
        plt.ylim(bottom=0)

    # Destaca o melhor ponto no gráfico
    if valores_fitness:
        min_fitness = min(valores_fitness)
        # Encontra o índice da primeira ocorrência do melhor fitness
        indice_min = valores_fitness.index(min_fitness)
        geracoes_min = valores_geracoes[indice_min]
        
        # Adiciona um ponto vermelho e um texto para destacar o melhor resultado (usando .format())
        plt.plot(geracoes_min, min_fitness, 'ro', markersize=3)
        # Adiciona um texto para destacar o melhor resultado, sem seta
        plt.text(geracoes_min, min_fitness + 5, # Coordenadas do texto
                f'{min_fitness},{geracoes_min}', # O texto a ser exibido
                ha='center') # Alinhamento horizontal

    plt.tight_layout() # Ajusta o layout para evitar que os rótulos se sobreponham
    plt.show()

'''
    Função main:
        Lê um arquivo de log, extrai os dados de geração e fitness e exibe o gráfico diretamente
        ou mensagens de erro. O script espera um argumento de linha de comando com o caminho para o arquivo.
'''

def main():
    # Verifica se o caminho do arquivo foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Erro: Forneça o caminho do arquivo como argumento.")
        return

    referencia = sys.argv[1]
    
    valores_geracoes = []
    valores_fitness = []

    try:
        with open(referencia, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Usa expressões regulares para encontrar os números de forma robusta
                match = re.search(r'Geracao:\s*(\d+),\s*fitness:\s*(\d+)', linha, re.IGNORECASE)
                
                if match:
                    # Extrai os valores encontrados
                    geracao = int(match.group(1))
                    fitness = int(match.group(2))
                    
                    valores_geracoes.append(geracao)
                    valores_fitness.append(fitness)
        
        # Verifica se algum dado foi encontrado antes de tentar plotar
        if not valores_geracoes:
            print(f"Nenhum dado no formato esperado foi encontrado em '{referencia}'.")
            return
            
        plotar_grafico(valores_geracoes, valores_fitness)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{referencia}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
