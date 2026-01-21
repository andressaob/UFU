import java.util.ArrayList;
import java.util.Calendar;

public class ReuniaoPresencial extends Reuniao {
    private ArrayList<String> itensP;
    public ReuniaoPresencial(int idReuniao, String email, String descricao, String tema, ArrayList<String> participantes,
                             ArrayList<String> itensP, ArrayList<Calendar> sugestaoDatas){
        super(idReuniao, email, descricao, tema, participantes, sugestaoDatas);
        this.itensP = itensP;
    }
    public ArrayList<String> getItensP(){
        return itensP;
    }

    public String mostraDados(){
        return "Id da reuniao presencial: "+getIdReuniao()+"\nEmail do criador: "+getEmailCriador()+"\nTema: "
                +getTema()+"\nDescricao: "+getDescricao()+"\n";
    }
}