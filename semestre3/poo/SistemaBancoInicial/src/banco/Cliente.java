package banco;

public class Cliente {
    static int ct = 0;
    String nome, CPF, telefone;
    int idade;
    Conta conta;
    
    public Conta getConta() {
        return conta;
    }
    
    public String mostraDadosConta() {
        String r = "";
        r += conta.num+" ";
        r += nome+" ";
        r += conta.saldo;
        return r;
    }
    
    public void cadastraCliente(String n, String cpf, String t, int i, Conta c) {
        nome = n;
        CPF = cpf;
        telefone = t;
        idade = i;
        conta = c;
        ct++;
    }
    
    public boolean estaNegativado() {
        return conta.ehNegativo();
    }
    
}