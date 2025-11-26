package tarefa4;

public class Administrativos extends Funcionario {
    public double horaExtra;
    public double salarioHora;
    public double salarioTotal;
    public double sa;
    
    public Administrativos(String nome, String rg){
        horaExtra = 1/100;
        salarioBase = sa;
    }
    
    public void alteraHoraExtra(double horaExtra){
        this.horaExtra = horaExtra;
    }
    public double retornaHoraExtra(){
        return horaExtra;
    }
    
    public double retornaSalarioHora(double salarioHora){
        return salarioHora;
    }
    
    public void alteraSalarioTotal(double salarioTotal){
        this.salarioTotal = salarioTotal;
    }
    public double retornaSalarioTotal(double salarioHora){
        double valorAcumulado = horaExtra*salarioHora;
        salarioTotal = valorAcumulado+salarioBase;
        valorAcumulado = 0;
        return salarioTotal;
    }
    
    public String mostrarFuncionariosAdministrativos(){
        return "Nome do funcionario: "+nome+"    RG do funcionario: "+rg;
    }
    
}
