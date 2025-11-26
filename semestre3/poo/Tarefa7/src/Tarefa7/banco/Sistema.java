package Tarefa7.banco;

import Tarefa7.Excecoes.ClienteExcecao;
import Tarefa7.Excecoes.ContaExcecao;
import Tarefa7.Excecoes.SistemaExcecao;
import Tarefa7.banco.Conta;
import Tarefa7.banco.Cliente;
import java.util.Scanner;

public class Sistema {
    
    private static Cliente[] clientes = new Cliente[10];
    private static int contClientes = 0;
    private static Cliente sessao;
    
    static void logar(Scanner sc) throws SistemaExcecao{
        System.out.print("Usuario: ");
        String usr = sc.nextLine();
        System.out.print("Senha: ");
        String sen = sc.nextLine();
        for (int i=0;i<contClientes;i++)
            if ((clientes[i].getConta().getUsuario().equals(usr))&&(clientes[i].getConta().getSenha().equals(sen)))
                sessao = clientes[i];
        if(sessao == null) throw new SistemaExcecao("Cliente nao encontrado!");
    }
    
    static Conta buscaConta(int num) throws SistemaExcecao{
        for (int i=0;i<contClientes;i++)
            //if (clientes[i].getNumConta() == num)
            if (clientes[i].getConta().getNum() == num)
                return clientes[i].getConta();
        throw new SistemaExcecao("Conta nao encontrada.");
    }
    
    public static void main(String a[]) throws ContaExcecao {
        Scanner sc = new Scanner(System.in);
        int op = -1;
        int contClientes = 0;
        
        while (op != 10) {
            System.out.println("=== MENU ===");
            System.out.println("1 - Cadastrar;");
            System.out.println("2 - Saldo;");
            System.out.println("3 - Sacar;");
            System.out.println("4 - Depositar;");
            System.out.println("5 - Transferir;");
            System.out.println("6 - Relatorio;");
            System.out.println("7 - Clientes negativados;");
            System.out.println("8 - Clientes com idade em intervalo;");
            System.out.println("9 - Encerrar sessao;");
            System.out.println("10 - Sair;");
            op = sc.nextInt();
            sc.nextLine();
            String tipo;
            float saldo;
            String nome, CPF, telefone;
            int idade;
            String usr,sen;
            Cliente c;
            
            switch(op) {
                case 1:
                    try{
                        System.out.print("Tipo da Conta: ");
                        tipo = sc.nextLine();
                        System.out.print("Saldo inicial: ");
                        saldo = sc.nextFloat();
                        sc.nextLine();                    
                        System.out.print("Nome: ");
                        nome = sc.nextLine();
                        System.out.print("CPF: ");
                        CPF = sc.nextLine();
                        System.out.print("Telefone: ");
                        telefone = sc.nextLine();
                        System.out.print("Idade: ");
                        idade = sc.nextInt();
                        sc.nextLine();
                        System.out.print("Usuario: ");
                        usr = sc.nextLine();
                        System.out.print("Senha: ");
                        sen = sc.nextLine();
                        Conta c1 = new Conta(tipo, usr, sen, saldo);
                        Cliente cli1 = new Cliente(nome, CPF, telefone, idade, c1);
                        clientes[contClientes] = cli1;
                        contClientes++;
                    }catch (ClienteExcecao e) {
                        System.out.println("Cliente: "+e.getMessage());
                    }catch (ContaExcecao e){
                        System.out.println("Conta: "+e.getMessage());
                    }catch (Exception e){
                        System.out.println("Geral: "+e.getMessage());
                    }
                    break;
                case 2:
                    try{
                        if(sessao == null) logar(sc);
                        System.out.println(sessao.getConta().mostraSaldo());
                    }catch(SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }
                    break;
                case 3:
                    try{
                        if(sessao == null) logar(sc);
                        System.out.println("Valor: ");
                        Float valor = sc.nextFloat();
                        sessao.getConta().sacar(valor);
                        System.out.println("Saque realizado com sucesso.");
                    }catch (ContaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }catch (SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }
                    break;
                    case 4:
                    try{
                        if(sessao == null) logar(sc);
                        System.out.println("Valor: ");
                        Float valor = sc.nextFloat();
                        sessao.getConta().depositar(valor);
                        System.out.println("Deposito realizado com sucesso.");
                    }catch (SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }
                    break;
                case 5:
                    try{
                        if(sessao == null) logar(sc);
                        System.out.println("Num conta destino: ");
                        int n = sc.nextInt();
                        System.out.println("Valor: ");
                        Float valor = sc.nextFloat();
                        Conta temp = buscaConta(n);
                        if(temp != null) sessao.getConta().transferir(valor, temp);
                        else System.out.println("Conta destino: inexistente!");
                    }catch (ContaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }catch (SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }
                    break;
                case 6:
                    for (int i=0;i<contClientes;i++) {
                        System.out.println(clientes[i].mostraDadosConta());
                    }
                    break;
                case 7:
                    System.out.println("=== Clientes negativados ===");
                    for (int i=0;i<contClientes;i++) {
                        if (clientes[i].estaNegativado())
                            System.out.println(clientes[i].mostraDadosConta());
                    }
                    break;
                case 8:
                    System.out.print("Idade inicial: ");
                    int idi = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Idade final: ");
                    int idf = sc.nextInt();
                    sc.nextLine();
                    System.out.println("Clientes com idade entre "+idi+" e "+idf+" anos:");
                    for (int i=0;i<contClientes;i++) {
                        if ((clientes[i].getIdade() >= idi) && 
                            (clientes[i].getIdade() <= idf))
                            System.out.println(clientes[i].mostraDadosConta());
                    }
                    break;
                case 9:
                    sessao = null;
            }
        }
    }
}