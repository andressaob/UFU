package ExercicioA;

public class Usuario {
    private String nome, CPF, nascimento, sexo, conta, senha, email;
    private Boolean noticias;
    
    public Usuario(String nome, String CPF, String nascimento, String sexo, String conta, 
            String senha, String email, Boolean noticias){
        this.nome = nome;
        this.CPF = CPF;
        this.nascimento = nascimento;
        this.sexo = sexo;
        this.conta = conta;
        this.senha = senha;
        this.email = email;
        this.noticias = noticias;
    }
    
    public String getNome(){
        return nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public String getCPF(){
        return CPF;
    }
    public void setCPF(String CPF){
        this.CPF = CPF;
    }
    
    public String getNascimento(){
        return nascimento;
    }
    public void setNascimento(String nascimento){
        this.nascimento = nascimento;
    }
    
    public String getSexo(){
        return sexo;
    }
    public void setSexo(String sexo){
        this.sexo = sexo;
    }
    
    public String getConta(){
        return conta;
    }
    public void setConta(String conta){
        this.conta = conta;
    }
    
    public String getSenha(){
        return senha;
    }
    public void setSenha(String senha){
        this.senha = senha;
    }
    
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email = email;
    }
    
    public Boolean getNoticias(){
        return noticias;
    }
    public void setNoticias(Boolean noticias){
        this.noticias = noticias;
    }
}
