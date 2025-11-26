package Tarefa7.banco;

import Tarefa7.Excecoes.ContaExcecao;

public class Conta {    
    private static int ct = 0;
    private String tipo;
    private float saldo;
    private int num;
    private String usuario, senha;
    
    public Conta(String tipo, String usuario, String senha, float saldo) throws ContaExcecao {
        this.tipo = tipo;
        this.usuario = usuario;
        this.senha = senha;
        if(saldo >= 500) this.saldo = saldo;
        else throw new ContaExcecao("Saldo inicial invalido.");
        num = ct;
        ct++;
    }
    
    String mostraSaldo() {
        return "O saldo da conta num "+getNum()+", do tipo ("+getTipo()+") eh "+getSaldo()+" reais.";
    }
    
    void sacar(float valor) throws ContaExcecao{
        if (valor > saldo) throw new ContaExcecao("Saldo insuficiente."); 
        else saldo -= valor;
    }
    
    boolean depositar(float valor) {
        saldo += valor;
        return true;
    }
    
    boolean ehNegativo() {
        return (saldo < 0);
    }
    
    void transferir(float valor, Conta c) throws ContaExcecao{
        this.sacar(valor);
        c.depositar(valor);
        System.out.println("Transferencia concluida.");
    }
    
    public String getUsuario(){
        return usuario;
    }
    
    public String getTipo(){
        return tipo;
    }
    
    public String getSenha(){
        return senha;
    }
    
    public float getSaldo(){
        return saldo;
    }
    
    public int getNum(){
        return num;
    }
}