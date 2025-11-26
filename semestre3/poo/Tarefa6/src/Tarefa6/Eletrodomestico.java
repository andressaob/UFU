package Tarefa6;

public class Eletrodomestico implements Produto{
    private int id;
    private int anoProducao;
    private int unidade;
    private String categoria;
    private double preco;
    
    public Eletrodomestico(int id, int anoProducao, int unidade, String categoria, double preco){
        this.id = id;
        this.anoProducao = anoProducao;
        this.unidade = unidade;
        this.categoria = categoria;
        this.preco = preco;
    }
    
    public int id(){
        return id;
    }
    
    public int anoProducao(){
        return anoProducao;
    }
    
    public int unidadeVenda(){
        return unidade;
    }
    
    public String categoria(){
        return categoria;
    }
    
    public double preco(){
        return preco;
    }
}