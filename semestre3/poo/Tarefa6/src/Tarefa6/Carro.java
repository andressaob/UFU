package Tarefa6;

public class Carro implements Veiculo{
    private String marca;
    private String modelo;
    private String cor;
    private int potencia;
    
    public Carro (String marca, String modelo, String cor, int potencia){
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.potencia = potencia;
    }
    
    public String marca(){
        return marca;
    }
    
    public String modelo(){
        return modelo;
    }
    
    public String cor(){
        return cor;
    }
    
    public int potencia(){
        return potencia;
    }
    
    public String mostraDados(){
        return "Tipo de veiculo: carro, marca: "+marca+", modelo: "+modelo+", cor: "+cor+", potencia: "+potencia+".";
    }
}