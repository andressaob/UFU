package tarefa4;

public class Vendedores extends Funcionario{
    public double comissao;
    public double salarioTotal;
    public int nVendas;
    public double sv;
    
    public Vendedores(String nome, String rg){
        comissao = 0.05;
        salarioBase = sv;
    }
    
    public void alteraComissao(double comissao){
        this.comissao = comissao;
    }
    public double retornaComissao(){
        return comissao;
    }
    
    public double totalVendas( int nVendas){
        return nVendas;
    }
    
    public void alteraSalarioTotal(double salarioTotal){
        this.salarioTotal = salarioTotal;
    }
    public double retornaSalarioTotal(int nVendas){
        double valorAcumulado = nVendas*comissao;
        salarioTotal = valorAcumulado + salarioBase;
        valorAcumulado = 0;
        return salarioTotal;
    }
    
    public String mostrarFuncionariosVendedores(){
        return "Nome do funcionario: "+nome+"    RG do funcionario: "+rg;
    }
    
}