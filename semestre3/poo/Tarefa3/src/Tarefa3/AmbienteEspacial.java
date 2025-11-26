package Tarefa3;

import java.util.Scanner;

public class AmbienteEspacial {
    public static void main(String a[]){
        
        int op = -1, ct = 0;
        Scanner leitor = new Scanner(System.in);
        NaveEspacial nv[] = new NaveEspacial[5];
        
        do{
            System.out.println("\n=============MENU=============\n");
            System.out.println("1) Criar uma nova nave;");
            System.out.println("2) Exibir as naves existentes;");
            System.out.println("3) Parar nave;");
            System.out.println("4) Ligar nave;");
            System.out.println("5) Verificar se a velocidade de uma nave e maior que a velocidade de"
                    + " outra;");
            System.out.println("6) Sair;");
            System.out.print("OPCAO: ");
            op = leitor.nextInt();
            switch(op){
                    case 1:
                        System.out.print("\nDigite o nome da nave: ");
                        String sn = leitor.next();
                        nv[ct] = new NaveEspacial(sn);
                        ct++;
                       break;
                    case 2:
                        System.out.println("\n");
                        for(int i=0; i<ct; i++) System.out.println(nv[i].mostrarNave());
                        break;
                    case 3:
                        for(int i=0; i<ct; i++) System.out.println("["+i+"] - "+nv[i].mostrarNave());
                        System.out.print("\nDigite o numero da nave que deseja parar: ");
                        int naveQueVaiParar = leitor.nextInt();
                        nv[naveQueVaiParar].pararNave();
                        break;
                    case 4:
                        int auxNavesLigadas = 0;
                        for(int i=0; i<ct; i++){
                            if((nv[i].retornaVelocidade()) > 0) auxNavesLigadas ++;
                        }
                        if(auxNavesLigadas > 3){
                            System.out.println("\n\n\nSuperpopulacao de naves!\n");
                            break;
                        }else{
                            for(int i=0; i<ct; i++) System.out.println("["+i+"] - "+nv[i].mostrarNave());
                            System.out.print("\nDigite o numero da nave que deseja ligar: ");
                            int naveQueVaiLigar = leitor.nextInt();
                            System.out.print("\nDigite o numero da velocidade que vai atribuir a nave: ");
                            int vl = leitor.nextInt();
                            nv[naveQueVaiLigar].ligarNave(vl);
                            break;
                        }
                    case 5:
                        for(int i=0; i<ct; i++) System.out.println("["+i+"] - "+nv[i].mostrarNave());
                        System.out.println("\nDigite o numero das naves que quer comparar: ");
                        int n1 = leitor.nextInt();
                        int n2 = leitor.nextInt();
                        if((nv[n1].naveMaisRapida(nv[n2])) == 1) System.out.println("\nA nave "
                                +"espacial "+nv[n1].retornaNome()+" e mais rapida do que a nave espacial "
                                +nv[n2].retornaNome()+".\n");
                        else if((nv[n1].naveMaisRapida(nv[n2])) == -1) System.out.println("\nA nave"
                                + " espacial "+nv[n1].retornaNome()+" tem a mesma velocidade que a nave "
                                        + "espacial "+nv[n2].retornaNome()+".\n");
                        else System.out.println("\nA nave espacial "+nv[n1].retornaNome()+" e mais lenta do"
                                + " que a nave espacial "+nv[n2].retornaNome()+".\n");
            }           
        }while(op != 6);
        
    }
}
