package Tarefa6;

public class Gerente extends Funcionario {
   
    public Gerente(String nome, String matricula, double salario_base){
        super(nome, matricula, salario_base);
    }
   
    public double calculaSalario(){
        return 2*getSalarioBase();
    }
   
    public String exibeDados(){
        return super.exibeDados()+", salario total: "+calculaSalario();
    }
}