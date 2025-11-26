package tarefa4;

public class Funcionario {

    public String nome;
    public String rg;
    public double salarioBase;
    
    public void alteraNome(String nome){
        this.nome = nome;
    }
    public String retornaNome(){
        return nome;
    }
    
    public void alteraRG(String rg){
        this.rg = rg;
    }
    public String retornaRG(){
        return rg;
    }
    
    public void alteraSalarioBase(double salarioBase){
        this.salarioBase = salarioBase;
    }
    public double retornaSalarioBase(){
        return salarioBase;
    }
    
}
