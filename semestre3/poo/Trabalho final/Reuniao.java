import java.util.ArrayList;
import java.util.Calendar;
import java.util.Map;

public abstract class Reuniao {
    private int idReuniao;
    private String email;
    //email de quem criou a reuniao
    private String descricao;
    private String tema;
    private ArrayList<String> participantes;
    private ArrayList<Calendar> sugestaoDatas;

    public Reuniao(int idReuniao, String email, String descricao, String tema, ArrayList<String> participantes,
                   ArrayList<Calendar> sugestaoDatas){
        this.idReuniao = idReuniao;
        this.descricao = descricao;
        this.tema = tema;
        this.participantes = participantes;
        this.email = email;
        this.sugestaoDatas = sugestaoDatas;
    }

    public int getIdReuniao(){
        return idReuniao;
    }

    public String getDescricao(){
        return descricao;
    }

    public String getTema(){
        return tema;
    }

    public ArrayList<String> getParticipantes() {
        return participantes;
    }

    public String getEmailCriador(){ return email; }

    public ArrayList<Calendar> getSugestaoDatas(){
        return sugestaoDatas;
    }

    //encontrando a data escolhida
    public Calendar getData(Reuniao r, Calendar dataEscolhida, Map<Calendar, Integer> votos){
        dataEscolhida = null;
        int maxVotos = -1;
        for (Map.Entry<Calendar, Integer> entry : votos.entrySet()) {
            //entrySet() retorna o conjunto de Maps contido no mapa
            Calendar data = entry.getKey(); //getKey() retorna a chave de cada valor
            int votosData = entry.getValue(); //getValue() retorna o valor de cada chave

            if (votosData > maxVotos) {
                maxVotos = votosData;
                dataEscolhida = data;
            }
        }
        return dataEscolhida;
    }

    public String getAgendaDiaria(Reuniao reuniao, Calendar data, Map<Calendar, Integer> votos){
        String agendaDiaria = "";

        Calendar dataDiaria = getData(reuniao, data, votos);
        if ((dataDiaria.get(Calendar.DAY_OF_MONTH) == data.get(Calendar.DAY_OF_MONTH)) && (dataDiaria.get(Calendar.MONTH) == data.get(Calendar.MONTH))  && (dataDiaria.get(Calendar.YEAR) == data.get(Calendar.YEAR))) {
            agendaDiaria += mostraDados();
        }

        if((agendaDiaria.equals(""))) return "Voce nao possui nenhuma reuniao hoje.\n";
        else return agendaDiaria;
    }

    public String getAgendaSemanal(Reuniao reuniao, Calendar data, Map<Calendar, Integer> votos){
        String agendaSemanal = "";
        Calendar dataSemanal = getData(reuniao, data, votos);

        if ((dataSemanal.get(Calendar.WEEK_OF_YEAR) == data.get(Calendar.WEEK_OF_YEAR))
                && (dataSemanal.get(Calendar.MONTH) == data.get(Calendar.MONTH))
                && (dataSemanal.get(Calendar.YEAR) == data.get(Calendar.YEAR))
        ) {
            agendaSemanal += mostraDados();
        }

        if((agendaSemanal.equals(""))) return "Voce nao possui nenhuma reuniao essa semana.\n";
        else return agendaSemanal;
    }

    public String getAgendaMensal(Reuniao reuniao, Calendar data, Map<Calendar, Integer> votos){
        String agendaMensal = "";

        Calendar dataMensal = getData(reuniao, data, votos);

        if (((dataMensal.get(Calendar.MONTH) == data.get(Calendar.MONTH))
                && (dataMensal.get(Calendar.YEAR) == data.get(Calendar.YEAR)))) {
            agendaMensal += mostraDados();
        }

        if((agendaMensal.equals(""))) return "Voce nao possui nenhuma reuniao esse mes.\n";
        else return agendaMensal;
    }
    public abstract String mostraDados();
}