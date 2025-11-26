package ExerciciosD;

import ExerciciosAeB.ContatoNaoEncontradoException;
import java.util.ArrayList;
import java.util.Scanner;

public class GestaoContatos {
    ArrayList<Contato> familia = new ArrayList<>();
    ArrayList<Contato> amigos = new ArrayList<>();
    ArrayList<Contato> profissional = new ArrayList<>();
    Scanner leitor = new Scanner(System.in);
    
    public void adicionaContato(String nome, int idade,  String sexo, String profissao, String telefone, String email){
        System.out.println("Digite FAMILIA caso queira adicionar esse contato aos contatos "
                + "familiares, AMIGOS caso queira adicionar esse contato aos contatos de amigos e"
                + " PROFISSIONAL caso queira adicionar esse contato aos contatos de ambito profissional.");
        String classe = leitor.next();
        if("FAMILIA".equals(classe)) familia.add(new Contato(nome, idade, sexo, profissao, telefone, email));
        else if("AMIGOS".equals(classe)) amigos.add(new Contato(nome, idade, sexo, profissao, telefone, email));
        else if("PROFISSIONAL".equals(classe)) profissional.add(new Contato(nome, idade, sexo, profissao, telefone, email));
        else System.out.println("Nao reconhecido.");
    }
    
    public void eliminaContato(String nome) throws ContatoNaoEncontradoException{
        int f=10, a=10, p=10;
        for(Contato em : familia)
            if(em.getNome().equals(nome))
                familia.remove(em);
            else f=0;
        for(Contato em : amigos)
            if(em.getNome().equals(nome))
                amigos.remove(em);
            else a=0;
        for(Contato em : profissional)
            if(em.getNome().equals(nome))
                profissional.remove(em);
            else p=10;
        if((a==0)&&(f==0)&&(p==0)){
            throw new ContatoNaoEncontradoException("Contato nao encontrado.");
        }
    }
    
    public void listaContatos(String classe){
        if("FAMILIA".equals(classe))
            for(Contato em : familia)
                System.out.println("- "+em);
        else if("AMIGOS".equals(classe))
            for(Contato em : amigos)
                System.out.println("- "+em);
        else if("PROFISSIONAL".equals(classe))
            for(Contato em : profissional)
                System.out.println("- "+em);
        else System.out.println("Nao reconhecido.");
    }
    
    public void toString(String classe){
        if("familia".equals(classe)){
            for(Contato em : familia)
            System.out.println("- "+em);
        }
        else if("amigos".equals(classe)){
            for(Contato em : amigos)
            System.out.println("- "+em);
        }
        else{
            for(Contato em : profissional)
            System.out.println("- "+em);
        }
    }
    
    public void maisVelho(String classe ){
        int idade = 0;
        String nome = "a";
        if("FAMILIA".equals(classe)){
            for(Contato em : familia){
                if(em.getIdade() > idade){
                    idade = em.getIdade();
                    nome = em.getNome();
                }
            }
            System.out.println("O contato mais velho da lista "+classe+" e o "+nome+".");
        }
        if("AMIGOS".equals(classe)){
            for(Contato em : amigos){
                if(em.getIdade() > idade){
                    idade = em.getIdade();
                    nome = em.getNome();
                }
            }
            System.out.println("O contato mais velho da lista "+classe+" e o "+nome+".");
        }
        if("PROFISSIONAL".equals(classe)){
            for(Contato em : profissional){
                if(em.getIdade() > idade){
                    idade = em.getIdade();
                    nome = em.getNome();
                }
            }
            System.out.println("O contato mais velho da lista "+classe+" e o "+nome+".");
        }
    }
    
    public void maisNovo(String classe){
        int idade = 150;
        String nome = "a";
        if("FAMILIA".equals(classe)){
            for(Contato em : familia){
                if(em.getIdade() < idade){
                    idade = em.getIdade();
                    nome = em.getNome();
                }
            }
            System.out.println("O contato mais novo da lista "+classe+" e o "+nome+".");
        }
        if("AMIGOS".equals(classe)){
            for(Contato em : amigos){
                if(em.getIdade() < idade){
                    idade = em.getIdade();
                    nome = em.getNome();
                }
            }
            System.out.println("O contato mais novo da lista "+classe+" e o "+nome+".");
        }
        if("PROFISSIONAL".equals(classe)){
            for(Contato em : profissional){
                if(em.getIdade() < idade){
                    idade = em.getIdade();
                    nome = em.getNome();
                }
            }
            System.out.println("O contato mais novo da lista "+classe+" e o "+nome+".");
        }
    }
}