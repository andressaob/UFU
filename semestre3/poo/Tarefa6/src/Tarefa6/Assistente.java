package Tarefa6;

public class Assistente extends Funcionario{
   
    public Assistente(String nome, String matricula, double salario_base){
        super(nome, matricula, salario_base);
    }
   
    public double calculaSalario(){
        return getSalarioBase();
    }
   
    public String exibeDados(){
        return super.exibeDados()+", salario total: "+calculaSalario();
    }
}