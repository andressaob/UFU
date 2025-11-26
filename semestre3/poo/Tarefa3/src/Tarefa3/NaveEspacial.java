package Tarefa3;   

import java.util.Random;

public class NaveEspacial {
    private String nome;
    private int velocidade;
    
    Random random = new Random();
    public NaveEspacial(String s){
        nome = s;
        velocidade = random.nextInt(5);
    }
    
    public void alteraNome(String novoNome){
        nome = novoNome;
    }
    public String retornaNome(){
        return nome;
    }
    public void alteraVelocidade(int novaVelocidade){
        velocidade = novaVelocidade;
    }
    public int retornaVelocidade(){
        return velocidade;
    }
    
    public String mostrarNave(){
        if(velocidade == 0) return "Nome da nave: "+nome+"    Nave inoperante";
        return "Nome da nave: "+nome+"    Velocidade da nave: "+velocidade;
    }
    
    public void pararNave(){
        alteraVelocidade(0);
    }
    
    public void ligarNave(int newVelocidade){
        alteraVelocidade(newVelocidade);
    }
    
    public int naveMaisRapida(NaveEspacial n2){
        if(velocidade > n2.retornaVelocidade()) return 1;
        else if(velocidade == n2.retornaVelocidade()) return -1;
        else return 0;
    }
}
