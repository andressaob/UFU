//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>
#define TAM 6

int main()
{

    int matriz[TAM][TAM], i, j, soma=0;

    //lendo a matriz
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            printf("matriz[%d][%d]= ", i, j); scanf("%3d", &matriz[i][j]);
        }
    }
    printf("\n\n");
    //imprimindo a matriz
    for(i=0; i<TAM; i++){
        printf("\n");
        for(j=0; j<TAM; j++){
            printf(" %3d", matriz[i][j]);
        }
    }
    printf("\n\n");
    //calculando a soma
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            if(i>j && i!=j)
                soma += matriz[i][j];
        }
    }

    //imprimindo a soma dos elementos abaixo da diagonal principal
    printf("Soma dos elementos abaixo da diagonal principal:\n%d", soma);

    return 0;
}
