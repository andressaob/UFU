public class Usuario {
    private String nomeCompleto;
    private String email;
    private String senha;

    public Usuario( String nomeCompleto, String email, String senha) {
        this.nomeCompleto = nomeCompleto;
        this.email = email;
        this.senha = senha;
    }

    public String getNomeCompleto(){
        return nomeCompleto;
    }

    public String getEmail(){
        return email;
    }

    public String getSenha(){
        return senha;
    }

    public String mostraDados(){
        return "Nome completo: "+nomeCompleto+", e email: "+email;
    }
}