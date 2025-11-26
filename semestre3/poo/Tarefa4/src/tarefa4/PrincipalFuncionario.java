package tarefa4;

import java.util.Scanner;

public class PrincipalFuncionario {
    public static void main(String a[]){
        
        int op = -1, cta = 0, ctv = 0;
        String nomeA, rgA, nomeV, rgV;
        Scanner leitor = new Scanner(System.in);
        Vendedores fv[] = new Vendedores[5];
        Administrativos fa[] = new Administrativos[5];
        
        do{
            System.out.println("\n============EMPRESA============\n");
            System.out.println("1) Cadastrar funcionario; ");
            System.out.println("2) Calcular salarios; ");
            System.out.println("3) Sair; ");
            System.out.print("OPCAO: ");
            op = leitor.nextInt();
            switch(op){
                case 1:
                    System.out.println("Digite 1 caso queira cadastrar um funcionario administrativo e "
                            + "2 caso queira cadastrar um funcionario vendedor: ");
                    op = leitor.nextInt();
                    switch(op){
                        case 1:
                            if(cta == 2) {
                                System.out.println("Numero de funcionarios administrativos foi "
                                    + "excedido.");
                                break;
                            }
                            System.out.println("Digite o nome do funcionario e numero do rg, "
                                    + "respectivamente:");
                            nomeA = leitor.next();
                            rgA = leitor.next();
                            fv[ctv] = new Vendedores(nomeA, rgA);
                            cta++;
                            break;
                        case 2:
                            if(ctv == 2) {
                                System.out.println("Numero de funcionarios vendedores foi "
                                    + "excedido.");
                                break;
                            }
                            System.out.println("Digite o nome do funcionario e numero do rg, "
                                    + "respectivamente:");
                            nomeV = leitor.next();
                            rgV = leitor.next();
                            fv[ctv] = new Vendedores(nomeV, rgV);
                            ctv++;
                            break;
                    }
                    break;
                case 2:
                    System.out.println("Digite 1 caso queira calcular o salario de um funcionario"
                            + " administrativo e 2 caso queira calcular o salario de um funcionario "
                            + "vendedor: ");
                    op = leitor.nextInt();
                    switch (op){
                        case 1:
                            for(int i=0; i<cta; i++) {
                                System.out.println("["+i+"] - "+fa[i].mostrarFuncionariosAdministrativos());
                            }
                            System.out.print("\nDigite o numero do funcionario que deseja calcular "
                                    + "o salario: ");
                            int nsfa = leitor.nextInt();
                            System.out.println("Digite o valor do salario por hora:");
                            int sha = leitor.nextInt();
                            System.out.println("O valor do salario total desse funcionario e: R$"
                                    + fa[nsfa].retornaSalarioTotal(sha));
                            break;
                        case 2:
                            for(int i=0; i<cta; i++) {
                                System.out.println("["+i+"] - "+fv[i].mostrarFuncionariosVendedores());
                            }
                            System.out.print("\nDigite o numero do funcionario que deseja calcular "
                                    + "o salario: ");
                            int nsfv = leitor.nextInt();
                            System.out.println("Digite o numero de vendas desse funcionario:");
                            int nv = leitor.nextInt();
                            System.out.println("O valor do salario total desse funcionario e: R$"
                                    + fa[nsfv].retornaSalarioTotal(nv));
                            break;
                    }
                    break;
            }
        }while(op != 3);
    }
}
