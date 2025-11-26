package Tarefa7;

import java.util.InputMismatchException;
import java.util.Scanner;

public class ExercicioC {
    public static void main(String a[]){
        int vetor[] = new int[10];
        int valor, indice, op;
        Scanner leitor = new Scanner(System.in);
        
        do{
            try{
                System.out.println("Insira um valor (inteiro):");
                valor = leitor.nextInt();
                System.out.println("Insira o indice do valor acima:");
                indice = leitor.nextInt();
                vetor[indice] = valor;
            }catch(InputMismatchException e){
                System.out.println("Erro, voce nao digitou um numero.");
            }catch(ArrayIndexOutOfBoundsException e){
                System.out.println("Erro, o indice que voce digitou nao existe no vetor.");
            }
            for(int i=0; i<10; i++){
                System.out.println("vetor["+i+"]= "+vetor[i]);
            }
            System.out.println("Digite 1 caso queira continuar inserindo valores no vetor e -1 "
                    + "caso queira parar a insercao.");
            op = leitor.nextInt();
        }while(op != -1);
    }
}
