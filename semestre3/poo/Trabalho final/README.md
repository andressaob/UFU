# Sistema de Gerenciamento de Reuniões

Um sistema em Java desenvolvido para gerenciar o agendamento de reuniões corporativas, permitindo o cadastro de usuários, criação de pautas, alocação de recursos e votação de datas entre os participantes.

## 📋 Sobre o Projeto

Este projeto é uma aplicação via console (CLI) que utiliza conceitos de Orientação a Objetos (Herança, Polimorfismo, Classes Abstratas) e manipulação de arquivos para persistência de dados. O sistema diferencia reuniões presenciais de virtuais, gerenciando os recursos necessários para cada tipo (ex: projetores para presenciais, tablets para virtuais).

## 🚀 Funcionalidades

* **Autenticação:** Cadastro de novos usuários e sistema de Login (Sessão).
* **Gestão de Reuniões:**
    * Criação de reuniões Presenciais ou Virtuais.
    * Definição de pauta, descrição e participantes.
    * Alocação de recursos (Coffe break, Sala, Computadores, etc.).
* **Sistema de Votação:**
    * O criador sugere datas possíveis.
    * Os participantes votam na melhor data.
    * O sistema identifica a data escolhida baseada na maioria dos votos.
* **Agenda:** Visualização de agenda Diária, Semanal e Mensal.
* **Persistência:** Os dados de usuários e reuniões são salvos automaticamente em arquivos locais (`.txt`).
* **Tratamento de Erros:** Sistema robusto com exceções personalizadas (`SistemaExcecao`).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Java
* **Entrada/Saída:** `java.io` (BufferedWriter, BufferedReader, File) para persistência de dados.
* **Datas:** `java.util.Calendar` e `SimpleDateFormat`.
* **Estruturas de Dados:** `ArrayList` e `HashMap`.

## 📂 Estrutura dos Arquivos

* `Sistema.java`: Classe principal contendo o método `main`, menus de interação e lógica de autenticação.
* `Usuario.java`: Representa os usuários do sistema.
* `Reuniao.java`: Classe abstrata que define a estrutura base de uma reunião e a lógica de votação.
* `ReuniaoPresencial.java`: Especialização para reuniões físicas (gerencia itens como sala e projetor).
* `ReuniaoVirtual.java`: Especialização para reuniões remotas (gerencia itens como computadores).
* `SistemaExcecao.java`: Classe de exceção personalizada para erros de lógica do sistema.

## ▶️ Como Executar

Certifique-se de ter o [JDK (Java Development Kit)](https://www.oracle.com/java/technologies/downloads/) instalado.

1.  **Compile os arquivos:**
    Abra o terminal na pasta do projeto e execute:
    ```bash
    javac *.java
    ```

2.  **Execute o sistema:**
    ```bash
    java Sistema
    ```

