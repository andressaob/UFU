package Tarefa3;

public class MaquinaPassagens {
    private int preco;
    private int quantidadeInserida;
    private int total;
    private String id;
    private int quantidadeTickets;
   
    public MaquinaPassagens(String i, int valor){
        preco = valor;
        quantidadeInserida = 0;
        total = 0;
        id = i;
        quantidadeTickets = 0;
    }
   
    public void alteraQtdInserida(int novaQtdInserida){
        quantidadeInserida = novaQtdInserida;
    }
    public int retornaQtdInserida(){
        return quantidadeInserida;
    }
   
    public void alteraTotal(int novoTotal){
        total = novoTotal;
    }
    public int retornaTotal(){
        return total;
    }
   
    public void alteraQtdtickets(int novaQtdTickets){
        quantidadeTickets = novaQtdTickets;
    }
   
    public void emiteTicket(int quantidadeTickets){
        for(int i=0; i< quantidadeTickets; i++){
            System.out.println("\n======\nTICKET\n======\n");
        }
    }
   
    public void insereDinheiro(int dinheiro, int qtdTickets){
        quantidadeTickets = qtdTickets; 
        quantidadeInserida += dinheiro; //20
        total += dinheiro; //20
        if(quantidadeInserida < (preco * quantidadeTickets)){
            System.out.println("Valor insuficiente. Insira mais R$"
                    +((preco * quantidadeTickets)-quantidadeInserida)+".");
        }else{
            quantidadeInserida -= (preco * quantidadeTickets); //aqui já é o troco
            emiteTicket(quantidadeTickets);
            if(quantidadeInserida > 0){
                System.out.println("Troco: R$"+quantidadeInserida+".");
                total -= quantidadeInserida;
                quantidadeInserida = 0;
            }
        }
    }
    
    public String mostraDados(){
        return preco+"\n\nId: "+id+"\nPreco: "+preco+"\nTotal: "+total+"\n\n";
    }
}