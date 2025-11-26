package ExerciciosD;

public class Contato {
    private String nome;
    private int idade;
    private String sexo;
    private String profissao;
    private String telefone;
    private String email;
    
    public Contato(String nome, int idade, String sexo, String profissao, String telefone, String email){
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
        this.profissao = profissao;
        this.telefone = telefone;
        this.email = email;
    }
    
    public String getNome(){
        return nome;
    }
    
    public int getIdade(){
        return idade;
    }
    
    public String getSexo(){
        return sexo;
    }
    
    public String getProfissao(){
        return profissao;
    }
    
    public String getTelefone(){
        return telefone;
    }
    
    public String getEmail(){
        return email;
    }
    
    public String toString(){
        return "<Nome> "+nome+", <Idade> "+idade+" anos, sexo "+sexo+" <Sexo>, <Profissão> "
                + ""+profissao+", telefone nº "+telefone+" <Telefone>, e-mail:"+email+" <Email> "+email+".";
    }
}
