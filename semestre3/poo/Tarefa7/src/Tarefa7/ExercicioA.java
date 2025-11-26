package Tarefa7;

import java.util.InputMismatchException;
import java.util.Scanner;

public class ExercicioA {

    public static void main(String[] args) {
    
        float numeroLido;
        boolean correto = false;
        int numeroTentativas = 0;
        Scanner leitor = new Scanner(System.in);
    
        while(correto == false && numeroTentativas < 3){
            System.out.print("Digite um número real: ");
            try{
                numeroLido = leitor.nextFloat();
                correto = true;
            }catch(InputMismatchException e){
                leitor.nextLine();
                System.out.println("Erro!");
                numeroTentativas++;
                if(numeroTentativas >= 3) System.out.println("Excedeu o limite de tentativas!");
            }
        }
    }
}
