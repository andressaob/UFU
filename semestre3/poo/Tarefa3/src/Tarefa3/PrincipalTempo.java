package Tarefa3;

import java.util.Scanner;

public class PrincipalTempo {
    public static void main(String a[]){
        Scanner leitor = new Scanner(System.in);
        int op = -1, hora, minuto, segundo;
        
        System.out.println("Parabéns pelo seu relogio novo!!!\nAgora, e so ajustar para poder "
                + "usar, digite a hora, o minuto e os segundos.");
        hora = leitor.nextInt();
        minuto = leitor.nextInt();
        segundo = leitor.nextInt();
        
        Tempo relogio = new Tempo(hora, minuto, segundo);
        
        do{
            System.out.println("\n\n========RELOGIO========");
            System.out.println("\n1) Formato de horas;");
            System.out.println("2) Ajuste minutos;");
            System.out.println("3) Sair;");
            System.out.print("OPCAO: ");
            op = leitor.nextInt();
            switch (op) {
                case 1:
                    System.out.println("\nDigite 1 caso queira ver a hora no formato 'hhmmss' ou 2 "
                            + "caso queira ver a hora no formato 'hh:mm:ss'");
                    op = leitor.nextInt();
                    switch(op){
                        case 1:
                            relogio.mostraTempoHMS();
                            break;
                        case 2:
                            relogio.mostraTempoH2PM2PS();
                            break;
                    }
                    break;
                case 2:
                    System.out.println("\nDigite 1 caso queira ajustar o ponteiro do minuto para +1 ou"
                            + " 2 caso queira ajustar para -1:");
                    op = leitor.nextInt();
                    switch(op){
                        case 1:
                            relogio.botaoMinutoMais();
                            break;
                        case 2:
                            relogio.botaoMinutoMenos();
                            break;
                    }
                    break;
            }
        }while (op != 3);
    }
}
