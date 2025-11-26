package Tarefa3;

public class Tempo {
    private int hora;
    private int minuto;
    private int segundo;
    
    public Tempo(int h, int m, int s){
        setHora(h);
        setMinuto(m);
        setSegundo(s);
    }
    
    public void setHora(int h){
        if(h > 0 && h < 24) hora = h;
        else hora = 0;
    }

    public void setMinuto(int m){
        if(m > 0 && m < 60) minuto = m;
        else minuto = 0;
    }
    
    public void setSegundo(int s){
        if(s > 0 && s < 60) segundo = s;
        else segundo = 0;
    }
    
    public void mostraTempoHMS(){
        System.out.println("\n\n"+hora+ +minuto+ +segundo+"\n\n");
    }
    
    public void mostraTempoH2PM2PS(){
        int auxHora = hora;
        switch(hora){
            case 13 : hora = 1; break;
            case 14 : hora = 2; break;
            case 15 : hora = 3; break;
            case 16 : hora = 4; break;
            case 17 : hora = 5; break;
            case 18 : hora = 6; break;
            case 19 : hora = 7; break;
            case 20 : hora = 8; break;
            case 21 : hora = 9; break;
            case 22 : hora = 10; break;
            case 23 : hora = 11; break;
            case 00 : hora = 12; break;
        }
        if(auxHora > 12) System.out.println("\n\n"+hora+":"+minuto+":"+segundo+" PM\n\n");
        else System.out.println("\n\n"+hora+":"+minuto+":"+segundo+" AM\n\n");
    }
    
    public void botaoMinutoMais(){
        if(minuto == 59){
            minuto = 00;
            hora ++;
        }
        else minuto ++;
    }
    
    public void botaoMinutoMenos(){
        if(minuto == 00 ){
            minuto = 59;
            hora --;
        }else minuto --;
    }    
}
