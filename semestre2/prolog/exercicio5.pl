%fatorial(Número, Fatorial = Resultado)
fatorial(0,1).                                           %caso base
fatorial(N,F) :- N>0,                                    %passo N>0, condição para números positivos
        N1 is N-1,                                       %simplifica o problema, fat de N = N * fat(N-1)
        fatorial(N1,F1),                                 %obtém a solução da instância menor
        F is N * F1,                                     %resultado final
        write("N = "), write(N), write(" Fat = "), writeln(F).  %imprime os resultados intermediários
fatorial(N) :- fatorial(N, F), write("Fat = "), writeln(F).     %permite a impressão do resultado final com apenas 1 termo
