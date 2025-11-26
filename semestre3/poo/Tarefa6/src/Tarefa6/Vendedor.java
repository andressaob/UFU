package Tarefa6;

public class Vendedor extends Funcionario{
   
    private double comissao;
   
    public Vendedor(String nome, String matricula, double salario_base, double comissao){
        super(nome, matricula, salario_base);
        this.comissao = comissao;
    }
   
    public double calculaSalario(){
        return getSalarioBase()+comissao;
    }
   
    public String exibeDados(){
        return super.exibeDados()+", comissao: "+comissao+ ", salario total: "+calculaSalario();
    }
}