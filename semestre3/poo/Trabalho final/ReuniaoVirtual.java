import java.util.ArrayList;
import java.util.Calendar;

public class ReuniaoVirtual extends Reuniao{
    private ArrayList<String> itensV;
    public ReuniaoVirtual(int idReuniao, String email, String descricao, String tema, ArrayList<String> participantes,
                          ArrayList<String> itensV, ArrayList<Calendar> sugestaoDatas){
        super(idReuniao, email, descricao, tema, participantes, sugestaoDatas);
        this.itensV = itensV;
    }

    public ArrayList<String> getItensV(){
        return itensV;
    }

    public String mostraDados(){
        return "Id da reuniao virtual: "+getIdReuniao()+"\nEmail do criador: "+getEmailCriador()+"\nTema: "
                +getTema()+"\nDescricao: "+getDescricao()+"\n";
    }
}