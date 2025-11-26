package Tarefa3;

import java.util.Scanner;

public class PrincipalMaquina {

    public static void main(String a[]){
    
        Scanner leitor = new Scanner(System.in);
        int op = -1;
        
        MaquinaPassagens M1 = new MaquinaPassagens("M1", 4);
        MaquinaPassagens M2 = new MaquinaPassagens("M2", 2);
        
        do{
            System.out.println("==========MENU==========");
            System.out.println("\n1) Comprar ticket;");
            System.out.println("2) Verificar montante;");
            System.out.println("3) Sair;");
            System.out.print("OPCAO: ");
            op = leitor.nextInt();
            switch (op) {
                case 1:
                    int qtdTickets;
                    float valorTickets;
                    System.out.println("\nMaquina de Passagens M1 - Valor da passagem: R$4\nMaquina "
                            + "de Passagens M2 - Valor da passagem R$2\nDigite o numero de qual máquina "
                            + "quer comprar:");
                    op = leitor.nextInt();
                    switch(op){
                        case 1:
                            int precoM1 = 4;
                            System.out.println("Digite a quantidade de tickets que deseja comprar:");
                            qtdTickets = leitor.nextInt();
                            System.out.println("Insira o dinheiro:");
                            int dinheiro1 = leitor.nextInt();
                            M1.insereDinheiro(dinheiro1, qtdTickets);
                            break;
                        case 2:
                            int precoM2 = 2;
                            System.out.println("Digite a quantidade de tickets que deseja comprar:");
                            qtdTickets = leitor.nextInt();
                            System.out.println("Insira o dinheiro:");
                            int dinheiro2 = leitor.nextInt();
                            M2.insereDinheiro(dinheiro2, qtdTickets);
                    }
                    break;
                case 2:
                    System.out.println("Digite o numero de qual maquina você quer ver o montante:");
                    op = leitor.nextInt();
                    switch(op){
                        case 1:
                            System.out.println(M1.mostraDados());
                            break;
                        case 2:
                            System.out.println(M2.mostraDados());
                            break;
                    }
                    break;
                case 3:
                    
            }
        }while (op != 3);
    }
}