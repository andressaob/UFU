package Tarefa6;

import java.util.Scanner;

public class PrincipalProduto {
    public static void main(String a[]){
        Produto p[] = new Produto[6];
        int i, op, ct=3;
        double total = 0;
        Scanner leitor = new Scanner(System.in);
        
        p[0] = new Eletrodomestico(15, 2022, 1, "eletrodomestico", 175);
        p[1] = new Vinho(96, 2018, 2, "vinho", 35);
        p[2] = new Cafe(5, 2023, 1, "cafe", 20);
        p[3] = null;
        p[4] = null;
        p[5] = null;
        
        do{
            System.out.println("\n1)Adicionar produto na lista;");
            System.out.println("2)Quantidade e preco total de determinada categoria;");
            System.out.println("3)Calcular o total dos produtos ja inseridos;");
            System.out.println("4)Sair;");
            System.out.print("OPCAO: ");
            op= leitor.nextInt();
            switch (op){
                case 1:
                    System.out.println("Digite o id do produto: ");
                    int idP = leitor.nextInt();
                    System.out.println("Digite o ano de producao: ");
                    int anoP = leitor.nextInt();
                    System.out.println("Digite quantas unidades: ");
                    int uP = leitor.nextInt();
                    System.out.println("Digite a categoria do produto (eletrodomestico, vinho, cafe): ");
                    String cP = leitor.next();
                    System.out.println("Digite o preco do produto: ");
                    double pP = leitor.nextDouble();
                    if((cP.equals("eletrodomestico"))||(cP.equals("Eletrodomestico"))){
                        p[ct] = new Eletrodomestico(idP, anoP, uP, cP, pP);
                        ct++;
                    }else if((cP.equals("vinho"))||(cP.equals("Vinho"))){
                        p[ct] = new Vinho(idP, anoP, uP, cP, pP);
                        ct++;
                    }else{
                        p[ct] = new Cafe(idP, anoP, uP, cP, pP);
                        ct++;
                    }
                    break;
                case 2:
                    System.out.println("Digite a categoria que deseja calcular a quantidade e preco total (vinho, eletrodomestico, cafe): ");
                    cP = leitor.next();
                    int ctE=0, ctV=0, ctC=0;
                    double pE=0, pV=0, pC=0;
                    for(i=0; i<ct; i++){
                        if(p[i] instanceof Eletrodomestico){
                            ctE+= p[i].unidadeVenda();
                            pE += (p[i].preco()*p[i].unidadeVenda());
                        }
                        if(p[i] instanceof Vinho){
                            ctV+= p[i].unidadeVenda();
                            pV += (p[i].preco()*p[i].unidadeVenda());
                        }
                        if(p[i] instanceof Cafe){
                            ctC+= p[i].unidadeVenda();
                            pC += (p[i].preco()*p[i].unidadeVenda());
                        }
                    }
                    if((cP.equals("eletrodomestico"))||(cP.equals("Eletrodomestico"))){
                        System.out.println("Quantidade: "+ctE+", preco total: R$"+pE);
                    }else if((cP.equals("vinho"))||(cP.equals("Vinho"))){
                        System.out.println("Quantidade: "+ctV+", preco total: R$"+pV);
                    }else{
                        System.out.println("Quantidade: "+ctC+", preco total: R$"+pC);
                    }
                    break;
                case 3:
                    for(i=0; i< ct; i++){
                        total += ((p[i].preco())*(p[i].unidadeVenda()));
                    }
                    System.out.println("Total da lista: R$"+total);
                    break;
            }
        } while (op != 4);
    }
}