package Tarefa6;

import java.util.Scanner;

public class PrincipalVeiculo {
    public static void main(String a[]){
        Veiculo v[] = new Veiculo[5];
        int i, op, menor=9999, maior=0;
        Scanner leitor = new Scanner(System.in);
        
        v[0] = new Carro("Ferrari", "HP", "vermelho", 830);
        v[1] = new Caminhao("Scania", "770 S V8", "amarelo", 770);
        v[2] = new Carro("Lamborghini", "Aventador", "vermelho", 780);
        v[3] = new Caminhao("Volvo", "FH16 750", "preto", 750);
        v[4] = new Caminhao("Mercedez Benz", "Actros", "vermelho", 630);
        
        do{
            System.out.println("\n1)Lista de veiculos;");
            System.out.println("2)Dentre os vermelhos, mostrar a marca do mais potente;");
            System.out.println("3)Dentre os vermelhos, mostrar a marca do menos potente;");
            System.out.println("4)Sair;");
            System.out.print("OPCAO: ");
            op= leitor.nextInt();
            switch (op){
                case 1:
                    for(i=0; i<5; i++){
                        System.out.println(v[i].mostraDados());
                    }
                    break;
                case 2:
                    String nVMaior = null;
                    for(i=0; i<5; i++){
                        if("vermelho".equals(v[i].cor())){
                            if((v[i].potencia())>maior){
                                maior = v[i].potencia();
                                nVMaior = v[i].marca();
                            }
                        }
                    }
                    if(maior>0) System.out.println( nVMaior);
                    break;
                case 3:
                    String nVMenor = null;
                    for(i=0; i<5; i++){
                        if("vermelho".equals(v[i].cor())){
                            if((v[i].potencia())<menor){
                                menor = v[i].potencia();
                                nVMenor = v[i].marca();
                            }
                        }
                    }
                    if(menor<9999) System.out.println( nVMenor);
                    break;
            }
        } while (op != 4);
    }
}