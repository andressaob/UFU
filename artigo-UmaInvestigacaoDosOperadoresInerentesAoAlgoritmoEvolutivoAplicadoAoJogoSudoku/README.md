# Solucionador de Sudoku via Algoritmo Genético (GA)

Este projeto implementa um Algoritmo Genético (AG) para encontrar soluções para tabuleiros de Sudoku. O sistema foi desenvolvido para ser performático utilizando compilação JIT (Just-In-Time) e inclui uma suíte de testes automatizados para experimentação de hiperparâmetros.

## 📂 Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- **`agSudoku.py`**: O núcleo do solucionador. Contém a classe `Individuo`, a lógica de avaliação de Fitness e os operadores genéticos (Crossover OX e Mutação Swap). O código é otimizado com a biblioteca `numba` para alta performance.

- **`testes.py`**: Script de automação que executa baterias de testes (Grid Search). Ele gera arquivos de configuração, executa o solucionador repetidamente com diferentes parâmetros e consolida os resultados.

## 🛠️ Pré-requisitos

Certifique-se de ter o Python 3.x instalado. As dependências do projeto são:

- **NumPy**: Para manipulação eficiente de arrays e matrizes.
- **Numba**: Para compilação JIT e aceleração matemática.
- **Matplotlib**: Para geração de gráficos (caso a função de plotagem seja ativada).

Para instalar todas as dependências:

```bash
pip install numpy numba
```

## 🚀 Como Executar

### 1. Execução do Solucionador (Modo Único)

Para tentar resolver um Sudoku com os parâmetros padrão definidos no código:

```bash
python agSudoku.py
```

**Entrada**: O script espera (ou cria) um arquivo binário `entradaArtigo.in` com os parâmetros e a matriz base.

**Saída**:
- Imprime o progresso da evolução (geração e fitness) no terminal.
- Ao encontrar a solução (Fitness 0), exibe a matriz resolvida.
- Gera `relatorioArtigo.txt` e `tempoExec.txt` com estatísticas da execução.

### 2. Execução da Bateria de Testes (Automação)

Para rodar múltiplos testes variando taxas de mutação, elitismo e tamanho de torneio:

```bash
python testes.py
```

- Este script irá iterar sobre as configurações definidas internamente.
- Os resultados serão salvos organizadamente na pasta `./resultados_testes`.
- Um relatório geral será criado em `./resultados_testes/relatorio_consolidado.txt`.

## 🧠 Detalhes do Algoritmo

### Representação

O cromossomo é representado por uma matriz 9x9 onde cada linha é uma permutação dos números de 1 a 9.

- **Vantagem**: Isso elimina a possibilidade de números repetidos nas linhas, reduzindo drasticamente o espaço de busca.
- **Objetivo**: O AG precisa apenas resolver os conflitos nas colunas e nos subgrids 3x3.

### Função de Fitness

O objetivo é minimizar o fitness (problema de minimização).

```
Fitness = Σ(repetições em colunas) + Σ(repetições em subgrids)
```

- Um fitness de **0** indica uma solução válida para o Sudoku.

### Operadores Genéticos

1. **Seleção por Torneio**: Seleciona K indivíduos aleatórios e escolhe o melhor para reprodução.

2. **Crossover OX (Order Crossover)**: Aplicado linha por linha independentemente. Preserva a ordem relativa dos genes e garante que a propriedade de permutação da linha seja mantida.

3. **Mutação (Swap)**: Troca dois números de posição dentro da mesma linha, respeitando as posições fixas (dicas iniciais) do tabuleiro.

4. **Elitismo**: Transfere os melhores indivíduos da geração atual diretamente para a próxima sem alterações.

## 📝 Notas Adicionais

- **Arquivos Binários**: A comunicação dos parâmetros entre o script de teste e o algoritmo genético é feita via arquivos binários (`.in`) utilizando a biblioteca `struct` para garantir integridade e rapidez.

- **Timeout**: O script de automação possui um timeout de segurança (padrão 180s) para evitar que execuções presas em ótimos locais travem a bateria de testes.

## 👨‍💻 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções ou novas funcionalidades.

---

**Desenvolvido com ❤️ usando Python, NumPy e Numba**
