package Tarefa7.banco;

import Tarefa7.Excecoes.ClienteExcecao;

public class Cliente {
    private static int ct = 0;
    private String nome, CPF, telefone;
    private int idade;
    private Conta conta;
    
    public Cliente(String nome, String CPF, String telefone, int idade, Conta conta) throws ClienteExcecao {
        this.nome = nome;
        this.CPF = CPF;
        this.telefone = telefone;
        if(idade<18) throw new ClienteExcecao("Cliente deve ser maior de idade.");
        else this.idade = idade;
        this.conta = conta;
        ct++;
    }
    
    public int getIdade(){
        return idade;
    }
    
    public Conta getConta() {
        return conta;
    }
    
    public String getNome(){
        return nome;
    }
    
    public String getTelefone(){
        return telefone;
    }
    
    public String getCPF(){
        return CPF;
    }
    
    public String mostraDadosConta() {
        String r = "";
        r += conta.getNum()+" ";
        r += nome+" ";
        r += conta.getSaldo();
        return r;
    }
    
    public boolean estaNegativado() {
        return conta.ehNegativo();
    }
}