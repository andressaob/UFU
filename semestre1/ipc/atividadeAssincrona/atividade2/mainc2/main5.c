//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int P, Q, i, j;
    printf("Coloque um valor para P, que será a quantidade de linhas: "); scanf("%d", &P);
    printf("\nColoque um valor para Q, que será a quantidade de colunas: "); scanf("%d", &Q);

    int M[P][Q], C[Q], L[P], soma;
    printf("\n\n");
    //lendo a matriz M
    for(i=0; i<P; i++){
        for(j=0; j<Q; j++){
            printf("M[%d][%d]= ", i, j); scanf("%3d", &M[i][j]);
        }
    }
    printf("\n");
    //imprimindo a matriz M
    for(i=0; i<P; i++){
        printf("\n");
        for(j=0; j<Q; j++){
            printf("%3d", M[i][j]);
        }
    }
    //calculando somatório das linhas da matriz M
    for(i=0; i<P; i++){
        soma=0; //inicializando a variável soma cada vez que a linha mudar
        for(j=0; j<Q; j++){
            soma = soma + M[i][j]; //somando linha por linha
        }
        L[i]= soma; /*calculando o vetor, quando acabar a primeira linha, vai voltar tudo de novo, incializar a
        variável soma, e somar a segunda linha e assim por diante.
        IMPORTANTE: perceber que o cálculo da soma está no segundo for, que vai variando as posições de cada linha.*/
    }
    //calculando o somatório das colunas da matriz M
    for(j=0; j<Q; j++){
        soma=0; //inicializando a variável soma cada vez que a COLUNA mudar
        for(i=0; i<P; i++){
            soma = soma + M[i][j]; //somando COLUNA por COLUNA
        }
        C[j]= soma; /*calculando o vetor, quando acabar a primeira COLUNA, vai voltar tudo de novo, incializar a
        variável soma, e somar a segunda COLUNA e assim por diante.
        IMPORTANTE: perceber que o cálculo da soma está no segundo for, que vai variando as posições de cada COLUNA.*/
    }
    printf("\n\n");
    //imprimindo os vetores L e C
    for(i=0; i<P; i++){
        printf("L[%d]= %3d\n", i, L[i]);
    }
    printf("\n");
    for(j=0; j<Q; j++){
        printf("C[%d]= %3d\n", j, C[j]);
    }

    return 0;
}
