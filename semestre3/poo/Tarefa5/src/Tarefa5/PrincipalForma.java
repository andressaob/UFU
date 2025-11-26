package Tarefa5;

import java.util.Scanner;

public class PrincipalForma {
    public static void main (String a[]){
        Scanner sc = new Scanner(System.in);
        Forma f[] = new Forma[10];
        int op, i;
        
        f[0] = new Circunferencia("amarelo", 10, 15, 5);
        f[1] = new Quadrado("azul", 12, 14, 10);
        f[2] = new Triangulo("vermelho", 7, 9, 2, 5);
        f[3] = new Esfera("verde", 3, 5, 7, 10);
        f[4] = new Cubo("laranja", 12, 14, 13, 12);
        f[5] = new Tetraedro("marrom", 25, 30, 20,  2, 3, 5);
        f[6] = new Triangulo("roxo", 1, 2, 9, 11);
        f[7] = new Cubo("cinza", 12, 13, 14, 8);
        f[8] = new Tetraedro("preto", 6, 7, 8, 2, 2, 4);
        f[9] = new Circunferencia("fucsia", 22, 25, 6);
        
        do{
            System.out.print("\n\n");
            System.out.println("2) Exibir formas cadastradas;");
            System.out.println("3) Mostrar área das formas bidimensionais cadastradas;");
            System.out.println("4) Mostrar o volume das formas tridimensionais cadastradas;");
            System.out.println("5) Existem duas esferas ou dois círculos que se interceptam");
            System.out.println("6) Sair;");
            System.out.print("OPCAO: ");
            op = sc.nextInt();
            switch (op){
                case 2:
                    System.out.print("\n");
                    for(i=0; i<9; i++)
                        System.out.println(f[i].exibeDados());
                    break;
                case 3:
                    System.out.print("\n");
                    for(i=0; i<10; i++){
                        if(f[i] instanceof FormaBidimensional)
                            System.out.println("Area: "+((FormaBidimensional)f[i]).obterArea());
                    }
                    break;
                case 4:
                    System.out.print("\n");
                    for(i=0; i<10; i++){
                        if(f[i] instanceof FormaTridimensional)
                            System.out.println("Volume: "+((FormaTridimensional)f[i]).obterVolume());
                    }
                    break;
                case 5:
                    System.out.print("\n");
                    System.out.println("Nao descobri como faz para saber se uma circunferencia/esfera intercepta"
                            + " a outra.");
            }
            
            
        }while(op != 6);
    }
    
}
