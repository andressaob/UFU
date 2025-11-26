package Tarefa6;

public abstract class Funcionario {
   
    private String nome;
    private String matricula;
    private double salario_base;
   
    public Funcionario(String nome, String matricula, double salario_base){
        this.nome = nome;
        this.matricula = matricula;
        this.salario_base = salario_base;
    }
   
    public double getSalarioBase(){
        return salario_base;
    }
   
    public abstract double calculaSalario();
   
    public String exibeDados(){
        return "Nome: "+nome+", matricula: "+matricula+", salario base: "+salario_base;
    }
}
