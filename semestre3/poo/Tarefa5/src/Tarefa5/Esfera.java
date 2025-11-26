package Tarefa5;

import static java.lang.Math.PI;

public class Esfera extends FormaTridimensional{

    private double raio;
   
    public Esfera(String cor, double coordenadaX, double coordenadaY, double coordenadaZ, double raio){
        super(cor, coordenadaX, coordenadaY, coordenadaZ);
        this.raio = raio;
    }
   
    public double obterVolume(){
        double volume = ((4/3)*PI*(raio*raio*raio));
        return volume;
    }
   
    public String exibeDados(){
        return super.exibeDados()+", raio: "+raio;
    }
}