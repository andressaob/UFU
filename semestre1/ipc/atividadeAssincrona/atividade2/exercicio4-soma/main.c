//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>
#define TAM 2

int main()
{
    int matrizA[TAM][TAM], matrizB[TAM][TAM], soma[TAM][TAM], i, j;

    //matrizA
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            matrizA[i][j] = 3*(i+1) + 4*(j+1);
        }
    }
    printf("matriz A:\n");
    //imprimindo matriz A
    for(i=0; i<TAM; i++){
        printf("\n");
        for(j=0; j<TAM; j++){
            printf(" %2d", matrizA[i][j]);
        }
    }
    printf("\n\n");
    //matrizB
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            matrizB[i][j] = -4*(i+1) -3*(j+1);
        }
    }
    printf("matriz B:\n");
    //imprimindo matriz B
    for(i=0; i<TAM; i++){
        printf("\n");
        for(j=0; j<TAM; j++){
            printf(" %2d", matrizB[i][j]);
        }
    }
    //calculando matriz soma
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            soma[i][j] = matrizA[i][j] + matrizB[i][j];
        }
    }
    printf("\n\n");
    printf("A matriz soma ficará da seguinte maneira:\n");
    //imprimindo matriz soma
    for(i=0; i<TAM; i++){
        printf("\n");
        for(j=0; j<TAM; j++){
            printf(" %2d", soma[i][j]);
        }
    }

    return 0;
}
