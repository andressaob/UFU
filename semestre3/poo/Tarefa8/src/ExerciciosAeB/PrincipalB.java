package ExerciciosAeB;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PrincipalB {
    public static void main(String a[]){
        
        ArrayList<EmpregadoB> v = new ArrayList<>();
        Map<String, EmpregadoB> empregados = new HashMap<String, EmpregadoB>();
        int op, numeroEmpregados = 0;
        Scanner leitor = new Scanner(System.in);
        
        do{
            System.out.println("1) Colocar os dados dos empregados na lista");
            System.out.println("2) Buscar um usuario dado o seu CPF");
            System.out.println("3) Mostrar os CPFs dos empregados com maior e menor salarios");
            System.out.println("4) Mostrar a lista de empregados");
            System.out.println("5) Sair");
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
                        empregados.put(CPF, new EmpregadoB(CPF, idade, salario));
                        v.add(new EmpregadoB(CPF, idade, salario));
                        numeroEmpregados++; 
                    }
                    break;
                case 2:
                    System.out.println("Digite o CPF do empregado que deseja buscar:");
                    CPF = leitor.next();
                    leitor.nextLine();
                    EmpregadoB e = buscaCPF(CPF, v);
                    if(e != null) System.out.println("- "+e);
                    else System.out.println("CPF nao encontrado.");
                    break;
                case 3:
                    float maiorSalario = 0;
                    float menorSalario = 99999999;
                    String CPFmaior = "000";
                    String CPFmenor = "000";
                    for(EmpregadoB em : v)
                        if(em.getSalario() > maiorSalario){
                            maiorSalario = em.getSalario();
                            CPFmaior = em.getCPF();
                        }
                    for(EmpregadoB em : v)
                        if(em.getSalario() < menorSalario){
                            menorSalario = em.getSalario();
                            CPFmenor = em.getCPF();
                        }
                    System.out.println("CPF do empregado com o maior salario: "+CPFmaior+" "
                            + "e CPF do empregado com menor salario: "+CPFmenor);
                    break;
                case 4:
                    System.out.println("Empregados:");
                    for(EmpregadoB em : v)
                        System.out.println("- "+em);
                    break;
            }
        }while(op != 5);
    }
    private static EmpregadoB buscaCPF(String CPF, ArrayList<EmpregadoB> v){
        for(EmpregadoB e : v)
            if(e.getCPF().equals(CPF))
                return e;
        return null;
    }
}
