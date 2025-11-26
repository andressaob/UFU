package ExerciciosAeB;

public class EmpregadoB implements Comparable{
    private String CPF;
    private int idade;
    private float salario;
   
    public EmpregadoB(String CPF, int idade, float salario){
        this.CPF = CPF;
        this.idade = idade;
        this.salario = salario;
    }
   
    public String getCPF(){
        return CPF;
    }
   
    public int getIdade(){
        return idade;
    }
   
    public float getSalario(){
        return salario;
    }
    
    public String toString(){
        return "CPF: "+CPF+", idade: "+idade+", salario: R$"+salario;
    }
    
    @Override
    public int compareTo(Object o){
        if(this.idade < ((EmpregadoB)o).getIdade()) return -1;
        if(this.idade > ((EmpregadoB)o).getIdade()) return 1;
        return 0;
    }
}
