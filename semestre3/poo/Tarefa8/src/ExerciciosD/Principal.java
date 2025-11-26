package ExerciciosD;

import ExerciciosAeB.ContatoNaoEncontradoException;
//import java.util.ArrayList;
import java.util.Scanner;

public class Principal {
    public static void main(String a[]) throws ContatoNaoEncontradoException{
        int op=0;
        Scanner leitor = new Scanner(System.in);
        int idade;
        String nome, email, telefone, sexo, profissao, classe;
        GestaoContatos g = new GestaoContatos();
        
        do{
            System.out.println("========================GESTAO DE CONTATOS========================");
            System.out.println("1)Adicionar contato;");
            System.out.println("2)Excluir contato;");
            System.out.println("3)Mostrar a lista de contatos (familiares, amigos ou profissional);");
            System.out.println("4)Mostrar a lista de TODOS os contatos;");
            System.out.println("5)Mostrar o nome do contato mais velho de uma lista de contatos"
                    + " especifica;");
            System.out.println("6)Mostrar o nome do contato mais novo de uma lista de contatos"
                    + " especifica;");
            System.out.println("7)Sair;");
            op = leitor.nextInt();
            switch(op){
                case 1:
                    System.out.println("Digite o nome do contato:");
                    nome = leitor.next();
                    System.out.println("Digite a idade do contato:");
                    idade = leitor.nextInt();
                    System.out.println("Digite o sexo do contato:");
                    sexo = leitor.next();
                    System.out.println("Digite a profissao do contato:");
                    profissao = leitor.next();
                    System.out.println("Digite o telefone do contato:");
                    telefone = leitor.next();
                    System.out.println("Digite o email do contato:");
                    email = leitor.next();
                    g.adicionaContato(nome, idade, sexo, profissao, telefone, email);
                    break;
                case 2:
                    System.out.println("Digite o nome do contato que voce deseja excluir:");
                    nome = leitor.next();
                    g.eliminaContato(nome);
                    break;
                case 3:
                    System.out.println("Digite FAMILIA para ver a lista de contatos familiares,"
                            + " AMIGOS para ver a lista de contatos de amigos ou PROFISSIONAL "
                            + "para ver a lista de contatos de ambito profissional.");
                    classe = leitor.next();
                    g.listaContatos(classe);
                    break;
                case 4:
                    g.toString("familia");
                    g.toString("amigos");
                    g.toString("profissional");
                    break;
                case 5:
                    System.out.println("Digite FAMILIA caso voce queira saber o nome do contato"
                            + " mais velho da lista de contatos familiares, AMIGOS caso voce queira"
                            + " saber o nome do contato mais velho da lista de contatos de amigos"
                            + " ou PROFISSIONAL caso voce queira saber o nome do contato mais "
                            + "velho da lista de contatos de ambito profissional.");
                    classe = leitor.next();
                    if((!"FAMILIA".equals(classe))&&(!"AMIGOS".equals(classe))&&(!"PROFISSIONAL".equals(classe)))
                        System.out.println("Erro, o que voce digitou nao e uma opcao!");
                    g.maisVelho(classe);
                    break;
                case 6:
                    System.out.println("Digite FAMILIA caso voce queira saber o nome do contato"
                            + " mais novo da lista de contatos familiares, AMIGOS caso voce queira"
                            + " saber o nome do contato mais novo da lista de contatos de amigos"
                            + " ou PROFISSIONAL caso voce queira saber o nome do contato mais "
                            + "novo da lista de contatos de ambito profissional.");
                    classe = leitor.next();
                    if((!"FAMILIA".equals(classe))&&(!"AMIGOS".equals(classe))&&(!"PROFISSIONAL".equals(classe)))
                        System.out.println("Erro, o que voce digitou nao e uma opcao!");
                    g.maisNovo(classe);
                    break;
            }
        }while(op != 7);
    }
    
}
