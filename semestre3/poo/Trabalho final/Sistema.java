import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Sistema {
    private static ArrayList<Reuniao> reunioes = new ArrayList<>();
    private static ArrayList<Usuario> usuarios = new ArrayList<>();
    private static Usuario sessao;

    static void logar(Scanner sc) throws SistemaExcecao{
        System.out.print("Email: ");
        String em = sc.nextLine();
        System.out.print("Senha: ");
        String sen = sc.nextLine();
        for (Usuario u : usuarios)
            if ((u.getEmail().equals(em)) && (u.getSenha().equals(sen)))
                sessao = u;
        if (sessao == null) throw (new SistemaExcecao("Usuario nao encontrado"));
    }

    public static void main(String a[]) {
        Scanner leitor = new Scanner(System.in);
        int op = -1;
        //variaveis utilizadas na main
        int idReuniao;
        String nomeCompleto, email, senha, tema, descricao;

        //listas de itens
        String itensPresencial[] = new String[4];
        itensPresencial[0] = new String("Projetor");
        itensPresencial[1] = new String("Coffe break");
        itensPresencial[2] = new String("Sala");
        itensPresencial[3] = new String("Endereco");

        String itensVirtual[] = new String[4];
        itensVirtual[0] = new String("Computadores");
        itensVirtual[1] = new String("Tablets");

        while (op != 10) {
            System.out.println("=== SISTEMA ===");
            System.out.println("1 - Cadastrar novo usuario");
            System.out.println("2 - Criar uma reuniao");
            System.out.println("3 - Ver as reunioes cadastradas na agenda do sistema");
            System.out.println("4 - Visualizar os usuarios cadastrados no sistema");
            System.out.println("5 - Consultar a minha agenda");
            System.out.println("6 - Votar em datas sugeridas das reunioes que sou participante");
            System.out.println("7 - Excluir usuario do sistema");
            System.out.println("8 - Excluir reuniao do sistema");
            System.out.println("9 - Encerrar sessao");
            System.out.println("10 - Sair");
            System.out.println("Caso nao apareca nenhuma reuniao, e porque nenhuma reuniao foi votada ainda!!!");
            op = leitor.nextInt();
            leitor.nextLine();
            switch (op) {
                case 1:
                    System.out.println("Digite o nome completo do novo usuario: ");
                    nomeCompleto = leitor.nextLine();
                    System.out.println("Digite o email: ");
                    email = leitor.next();
                    for (Usuario u : usuarios) {
                        do {
                            if (!email.equals(u.getEmail()))
                                break;
                            else {
                                System.out.println("Email ja esta em uso. Tente novamente!");
                                email = leitor.next();
                            }
                        } while (email.equals(u.getEmail()));
                    }
                    System.out.println("Digite a senha: ");
                    senha = leitor.next();

                    //criacao do arquivo txt usuario identificado pelo email
                    BufferedWriter escritor = null; //objeto escritor
                    try{
                        escritor = new BufferedWriter(new FileWriter(new File(email)));
                        //Instanciação do objeto escritor
                        escritor.write(nomeCompleto+"***"+email+"***"+senha);
                        //Gravação do texto
                        escritor.flush();
                        //descarga do buffer de escrita
                        escritor.close();
                        //fechamento do arquivo
                    }catch(IOException e){
                        e.printStackTrace();
                    }
                    usuarios.add(new Usuario(nomeCompleto, email, senha));
                    System.out.println("Novo usuario cadastrado no sistema! O email e a senha serao utilizados" +
                            " para fazer o login.\n");
                    break;
                case 2:
                    try {
                        ArrayList<String> participantes = new ArrayList<>();
                        ArrayList<String> itensP = new ArrayList<>();
                        ArrayList<String> itensV = new ArrayList<>();
                        ArrayList<Calendar> sugestaoDatas = new ArrayList<>();
                        Map<Calendar, Integer> votos = new HashMap<>();

                        if (sessao == null) logar(leitor);
                        System.out.println("Digite um id para a identificacao da nova reuniao: ");
                        idReuniao = leitor.nextInt();
                        leitor.nextLine();
                        for (Reuniao r : reunioes) {
                            do {
                                if (!(idReuniao == r.getIdReuniao()))
                                    break;
                                else {
                                    System.out.println("IdReuniao ja esta em uso. Tente novamente!");
                                    idReuniao = leitor.nextInt();
                                }
                            } while (idReuniao == r.getIdReuniao());
                        }
                        String emailCriadorReuniao = sessao.getEmail();
                        System.out.println("Digite o tema da reuniao: ");
                        tema = leitor.nextLine();
                        System.out.println("Digite a descricao da reuniao: ");
                        descricao = leitor.nextLine();
                        System.out.println("Digite o numero de participantes que voce quer na reuniao: ");
                        int numeroParticipante;
                        int ctParticipantes = 0;
                        numeroParticipante = leitor.nextInt();
                        System.out.println("Agora digite o/s email/s da/s pessoa/s que voce quer na reuniao: ");
                        while (ctParticipantes != numeroParticipante) {
                            email = leitor.next();
                            participantes.add(email);
                            ctParticipantes++;
                        }
                        System.out.println("Digite 1 caso voce queira criar uma reuniao presencial e 2 caso queira criar" +
                                " uma reuniao virtual.");
                        op = leitor.nextInt();
                        switch (op) {
                            case 1:
                                System.out.println("Lista de itens disponiveis para a locacao:");
                                for (int i = 0; i < 4; i++) {
                                    System.out.println(itensPresencial[i]);
                                }
                                System.out.println("Digite a quantidade de itens que deseja utilizar e o nome deles:");
                                int nItens, ctItens;
                                ctItens=0;
                                nItens = leitor.nextInt();
                                leitor.nextLine();
                                while (ctItens != nItens) {
                                    String item = leitor.next();
                                    itensP.add(item);
                                    ctItens++;
                                }
                                System.out.println("Agora e hora de digitar as sugestoes de datas. Precisarao ser sugeridas" +
                                        " 4 datas; digite o dia (do mes), o mes e o ano, respectivamente.");
                                int ctSugestoes = 0, nSugestoes = 2;
                                while (ctSugestoes != nSugestoes) {
                                    int dia, mes, ano;
                                    dia = leitor.nextInt();
                                    mes = leitor.nextInt();
                                    ano = leitor.nextInt();
                                    Calendar sugestao = Calendar.getInstance();
                                    sugestao.set(Calendar.DAY_OF_MONTH, dia);
                                    sugestao.set(Calendar.MONTH, mes-1); //em java o Calendar inicia a contagem dos meses no índice 0 até 11
                                    sugestao.set(Calendar.YEAR, ano);
                                    sugestaoDatas.add(sugestao);
                                    //inicializando a quantidade de votos para as datas sugeridas com 0
                                    votos.put(sugestao, 0);
                                    ctSugestoes++;
                                }

                                //cadastro das reunioes
                                escritor = null; //objeto escritor
                                try{
                                    escritor = new BufferedWriter(new FileWriter(new File(""+idReuniao)));
                                    //Instanciação do objeto escritor
                                    escritor.write(idReuniao+"***"+emailCriadorReuniao+"***"+descricao+"***"+tema+"***"+participantes);
                                    //Gravação do texto
                                    escritor.flush();
                                    //descarga do buffer de escrita
                                    escritor.close();
                                    //fechamento do arquivo
                                }catch(IOException e){
                                    e.printStackTrace();
                                }
                                reunioes.add(new ReuniaoPresencial(idReuniao, emailCriadorReuniao, descricao, tema, participantes, itensP, sugestaoDatas));

                                System.out.println("Sua reuniao presencial foi criada!\n");
                                break;
                            case 2:
                                System.out.println("Lista de itens disponiveis para a transmissao:");
                                for (int i = 0; i < 2; i++) {
                                    System.out.println(itensVirtual[i]);
                                }
                                System.out.println("Digite a quantidade de itens que deseja utilizar e o nome deles:");
                                ctItens = 0;
                                nItens = leitor.nextInt();
                                leitor.nextLine();
                                while (ctItens != nItens) {
                                    String item = leitor.next();
                                    itensV.add(item);
                                    ctItens++;
                                }
                                System.out.println("Agora e hora de digitar as sugestoes de datas. Precisarao ser sugeridas" +
                                        " 4 datas; digite o dia (do mes), o mes e o ano, respectivamente.");
                                ctSugestoes = 0;
                                nSugestoes = 2;
                                while (ctSugestoes != nSugestoes) {
                                    int dia, mes, ano;
                                    dia = leitor.nextInt();
                                    mes = leitor.nextInt();
                                    ano = leitor.nextInt();
                                    Calendar sugestao = Calendar.getInstance();
                                    sugestao.set(Calendar.DAY_OF_MONTH, dia);
                                    sugestao.set(Calendar.MONTH, mes-1); //em java o Calendar inicia a contagem dos meses no índice 0 até 11. mes digitado: 4 -> quer dizer que no Calendar é indice 3
                                    sugestao.set(Calendar.YEAR, ano);
                                    sugestaoDatas.add(sugestao);
                                    ctSugestoes++;
                                }

                                //cadastro das reunioes
                                escritor = null; //objeto escritor
                                try{
                                    escritor = new BufferedWriter(new FileWriter(new File(""+idReuniao)));
                                    //Instanciação do objeto escritor
                                    escritor.write(idReuniao+", "+emailCriadorReuniao+", "+descricao+", "+tema+", "+participantes);
                                    //Gravação do texto
                                    escritor.flush();
                                    //descarga do buffer de escrita
                                    escritor.close();
                                    //fechamento do arquivo
                                }catch(IOException e){
                                    e.printStackTrace();
                                }
                                reunioes.add(new ReuniaoVirtual(idReuniao, emailCriadorReuniao, descricao, tema, participantes, itensV, sugestaoDatas));
                                System.out.println("Sua reuniao virtual foi criada!\n");
                                break;
                        }
                    }catch (SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage()+"\n");
                    }catch (InputMismatchException ie){
                        System.out.println("Voce digitou algo nao numerico, tente novamente.\n");
                        leitor.nextLine();
                    }catch (Exception er){
                        System.out.println("Erro!\n");
                    }
                    break;
                case 3:
                    for (Reuniao r : reunioes){
                        String linha;
                        BufferedReader arquivo = null; //Objeto leitor
                        try {
                            arquivo = new BufferedReader(new FileReader(new File(""+r.getIdReuniao())));
                            //Instanciação do objeto leitor
                            while ((linha = arquivo.readLine()) != null) {
                                System.out.println("Id reuniao: "+r.getIdReuniao());
                                System.out.println("Email do criador: "+r.getEmailCriador());
                                System.out.println("Tema: "+r.getTema());
                                System.out.println("Descricao: "+r.getDescricao());
                                System.out.println("------------------------");
                            }
                            arquivo.close();
                            //fechamento do arquivo
                        } catch (java.io.IOException e) {
                            System.out.println("File error: " + e.toString());
                        }
                    }
                    break;
                case 4:
                    for (Usuario u : usuarios) {
                        String linha;
                        BufferedReader arquivo = null; //Objeto leitor
                        try {
                            arquivo = new BufferedReader(new FileReader(new File(u.getEmail())));
                            //Instanciação do objeto leitor
                            while ((linha = arquivo.readLine()) != null) {
                                System.out.println("Nome: " +u.getNomeCompleto());
                                System.out.println("Email: " +u.getEmail());
                                System.out.println("------------------------");
                            }
                            arquivo.close();
                            //fechamento do arquivo
                        } catch (java.io.IOException e) {
                            System.out.println("File error: " + e.toString());
                        }
                    }
                    break;
                case 5:
                    try {
                        Map<Calendar, Integer> votos = new HashMap<>();

                        if (sessao == null) logar(leitor);
                        System.out.println(("Digite 1 caso queira visualizar a sua agenda diaria, 2 caso queira visualizar" +
                                " a sua agenda semanal e 3 caso queira visualizar a sua agenda mensal:"));
                        op = leitor.nextInt();
                        switch (op) {
                            case 1:
                                System.out.println("Agenda diaria:");
                                Calendar data = Calendar.getInstance();
                                for (Reuniao r : reunioes)
                                    if ((r.getParticipantes().contains(sessao.getEmail()))||(r.getEmailCriador().equals(sessao.getEmail())))
                                        System.out.println(r.getAgendaDiaria(r, data, votos));
                                break;
                            case 2:
                                System.out.println("Agenda semanal:");
                                data = Calendar.getInstance();
                                for (Reuniao r : reunioes)
                                    if ((r.getParticipantes().contains(sessao.getEmail()))||(r.getEmailCriador().equals(sessao.getEmail())))
                                        System.out.println(r.getAgendaSemanal(r, data, votos));
                                break;
                            case 3:
                                System.out.println("Agenda mensal:");
                                data = Calendar.getInstance();
                                for (Reuniao r : reunioes)
                                    if ((r.getParticipantes().contains(sessao.getEmail()))||(r.getEmailCriador().equals(sessao.getEmail())))
                                        System.out.println(r.getAgendaMensal(r, data, votos));
                        }
                    }catch(SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }catch (InputMismatchException ie){
                        System.out.println("Voce digitou algo nao numerico, tente novamente.");
                        leitor.nextLine();
                    }catch (Exception er){
                        System.out.println("Erro!");
                    }
                    break;
                case 6:
                    try {
                        Map<Calendar, Integer> votos = new HashMap<>();
                        if (sessao == null) logar(leitor);
                        System.out.println("Visualizacao da agenda com todas as reunioes que participo:");

                        ArrayList<Reuniao> reunioesParticipantes = new ArrayList<>();

                        for (Reuniao r : reunioes) {
                            if (!(sessao.getEmail().equals(r.getEmailCriador())) && r.getParticipantes().contains(sessao.getEmail())){
                                reunioesParticipantes.add(r);
                                System.out.println(r.mostraDados());
                            }
                        }

                        if (reunioesParticipantes.size() == 0) {
                            System.out.println("Voce ainda nao participa de nenhuma reuniao ou a reuniao que voce participa" +
                                    " foi voce quem criou.");
                            break;
                        } else {
                            System.out.println("Digite o id da reuniao na qual deseja votar a data: ");
                            idReuniao = leitor.nextInt();
                            for (Reuniao r : reunioesParticipantes) {
                                if (r.getIdReuniao() == idReuniao) {

                                    for (Calendar sugestaoData : r.getSugestaoDatas()) {
                                        System.out.println(format(sugestaoData));
                                    }

                                    System.out.println("Digite o dia (do mes), mes e ano, respectivamente, da data que" +
                                            " deseja votar:");
                                    int dia, mes, ano;
                                    dia = leitor.nextInt();
                                    mes = leitor.nextInt();
                                    ano = leitor.nextInt();
                                    Calendar dataVotada = Calendar.getInstance();
                                    dataVotada.set(Calendar.DAY_OF_MONTH, dia);
                                    dataVotada.set(Calendar.MONTH, mes-1); //em java o Calendar inicia a contagem dos meses no índice 0 até 11. mes digitado: 4 -> quer dizer que no Calendar é indice 3
                                    dataVotada.set(Calendar.YEAR, ano);

                                    boolean validDate = false;

                                    for (Map.Entry<Calendar, Integer> entry : votos.entrySet()) {
                                        //entrySet() retorna o conjunto de Maps contido no mapa
                                        Calendar data = entry.getKey(); //getKey() retorna a chave de cada valor

                                        String dataVotosFormatada = format(data);

                                        if (format(dataVotada).equals(dataVotosFormatada)) {
                                            // Incrementar o voto para a data selecionada
                                            entry.setValue(entry.getValue()+1);
                                            System.out.println("Voto computado com sucesso!\n");
                                            validDate = true;
                                            break;
                                        }
                                    }

                                    if(!validDate) {
                                        System.out.println("Data inválida.\n");
                                    }

                                }
                            }
                        }
                    }catch (SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }catch (InputMismatchException ie){
                        System.out.println("Voce digitou algo nao numerico, tente novamente.");
                        leitor.nextLine();
                    }catch (Exception er){
                        System.out.println("Erro!");
                    }
                    break;
                case 7:
                    try {
                        if (sessao == null) logar(leitor);
                        System.out.println("Digite o email do usuario que quer excluir do sistema: ");
                        email = leitor.next();
                        File arquivo = new File(email);
                        for (Usuario u : usuarios)
                            if ((email.equals(u.getEmail()))) {
                                if (arquivo.delete())
                                    System.out.println("Usuario " + email + " foi descontinuado do sistema!\n");
                                else
                                    System.out.println("O email digitado nao esta no sistema.");
                            }
                    }catch(SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }catch (Exception er){
                        System.out.println("Erro!");
                    }
                    break;
                case 8:
                    try {
                        if (sessao == null) logar(leitor);
                        for (Reuniao r : reunioes){
                            if(r.getEmailCriador().equals(sessao.getEmail())){
                                System.out.println("Digite o id da reuniao que quer excluir do sistema: ");
                                idReuniao = leitor.nextInt();
                                File arquivo = new File(""+idReuniao);
                                if(arquivo.delete()) System.out.println("Reuniao com o id "+idReuniao+" foi excluida do sistema.");
                                else System.out.println("O id reuniao digitado nao esta no sistema.");
                            }
                        }
                    }catch(SistemaExcecao e){
                        System.out.println("Geral: "+e.getMessage());
                    }catch (Exception er){
                        System.out.println("Erro!");
                    }
                    break;
                case 9:
                    sessao = null;
                    System.out.println("Voce acaba de ser deslogado do sistema!\n");
                    break;
            }
        }
    }

    public static String format(Calendar date) throws ParseException {
        SimpleDateFormat patternDate = new SimpleDateFormat("dd-MM-yyyy");

        return patternDate.format(date.getTime());
    }
}
