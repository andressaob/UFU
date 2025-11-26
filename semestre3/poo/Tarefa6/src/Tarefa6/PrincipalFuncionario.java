package Tarefa6;

import java.util.Scanner;

public class PrincipalFuncionario {
    public static void main(String a[]){
       
        Funcionario f[] = new Funcionario[5];
        int i, op, ctA=0, ctG=0, ctV=0;
        double total=0;
        Scanner leitor = new Scanner(System.in);
       
        f[0] = new Gerente("Andressa", "01234", 2500);
        f[1] = new Vendedor("Anaysa", "12345", 1800, 600);
        f[2] = new Vendedor("Rayan", "23456", 1800, 550);
        f[3] = new Assistente("Analya", "345678", 1200);
        f[4] = new Assistente("Rael", "456789", 1200);
       
       
        do{
            System.out.println("\n1) Mostrar folha salarial;");
            System.out.println("2) Media salarial dos funcionarios;");
            System.out.println("3) Sair;");
            System.out.print("OPCAO; ");
            op = leitor.nextInt();
            switch (op){
                case 1:
                    for(i=0; i<5; i++){
                        System.out.println(f[i].exibeDados());
                        total+= f[i].calculaSalario();
                    }
                    System.out.println("Salário total: "+total);
                    break;
                case 2:
                    double salG=0, salA=0, salV=0;
                    for(i=0; i<5; i++){
                        if(f[i] instanceof Gerente){
                            ctG++;
                            salG += f[i].calculaSalario();
                        }
                        if(f[i] instanceof Assistente){
                            ctA++;
                            salA += f[i].calculaSalario();
                        }
                        if(f[i] instanceof Vendedor){
                            ctV++;
                            salV += f[i].calculaSalario();
                        }
                    }
                    if(ctG>0) System.out.println("Media salarial dos Gerentes: "+(salG/ctG));
                    else System.out.println("Sem Gerentes.");
                    if(ctA>0) System.out.println("Media salarial dos Assistentes: "+(salA/ctA));
                    else System.out.println("Sem Assistentes.");
                    if(ctG>0) System.out.println("Media salarial dos Vendedores: "+(salV/ctV));
                    else System.out.println("Sem Vendedores.");
                    break;
            }
        }while(op != 3);
    }
   
}