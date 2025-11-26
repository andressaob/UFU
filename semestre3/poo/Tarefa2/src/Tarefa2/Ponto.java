package Tarefa2;


public class Ponto {
    private float X, Y;
    
    public Ponto(float corX, float corY){
        if(corX < 0)
            corX = 0;
        X = corX;
        if(corY < 0)
            corY = 0;
        Y = corY;
    }
    
    public void alteraX(float novoX){
        X = novoX;
    }
    public float retornaX(){
        return X;
    }
    public void alteraY(float novoY) {
        Y = novoY;
    }
    public float retornaY(){
        return Y;
    }
    
    public float distanciaAB(Ponto P2){
        float D;
        /*calculo retirado do seguinte site: https://www.guj.com.br/t/calculo-distancia-processamento-de-imagens/116911 */
        D = (float) Math.sqrt(Math.sqrt(X - P2.X) + Math.sqrt(Y - P2.Y));
        return D;
    }
}