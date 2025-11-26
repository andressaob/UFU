package ExerciciosAeB;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class PrincipalA {
    public static void main(String a[]){
        
        ArrayList<EmpregadoA> v = new ArrayList<>();
        int op, numeroEmpregados = 0;
        Scanner leitor = new Scanner(System.in);
        
        do{
            System.out.println("1) Colocar os dados dos empregados na lista");
            System.out.println("2) Buscar um usuario dado o seu CPF");
            System.out.println("3) Pesquisa de salarios");
            System.out.println("4) Ordenar por idade");
            System.out.println("5) Mostrar a lista de empregados");
            System.out.println("6) Sair");
            op = leitor.nextInt();
            String CPF;
            int idade;
            float salario;
            switch(op){
                case 1:
                    if(numeroEmpregados == 5) System.out.println("Erro, nao tem como inserir mais empregados para a lista.");
                    else{
                        System.out.println("CPF:");
                        CPF = leitor.next();
                        System.out.println("Idade:");
                        idade = leitor.nextInt();
                        System.out.println("Salario:");
                        salario = leitor.nextFloat();
                        v.add(new EmpregadoA(CPF, idade, salario));
                        numeroEmpregados++; 
                    }
                    break;
                case 2:
                    System.out.println("Digite o CPF do empregado que deseja buscar:");
                    CPF = leitor.next();
                    leitor.nextLine();
                    
                    EmpregadoA e = buscaCPF(CPF, v);
                    if(e != null) System.out.println("- "+e);
                    else System.out.println("CPF nao encontrado.");
                    break;
                case 3:
                    System.out.println("Digite o salario que deseja buscar:");
                    salario = leitor.nextInt();
                    for(EmpregadoA em : v)
                        if(em.getSalario() > salario)
                            System.out.println("- "+em);
                    break;
                case 4: 
                    Collections.sort(v);
                    System.out.println("Colecao ordenada por idade!");
                    break;
                case 5:
                    System.out.println("Empregados:");
                    for(EmpregadoA em : v)
                        System.out.println("- "+em);
                    break;
            }
        }while(op != 6);
    }
    private static EmpregadoA buscaCPF(String CPF, ArrayList<EmpregadoA> v){
        for(EmpregadoA e : v)
            if(e.getCPF().equals(CPF))
                return e;
        return null;
    }
}
