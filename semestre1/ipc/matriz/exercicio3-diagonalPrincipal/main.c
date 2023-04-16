#include <stdio.h>
#include <stdlib.h>
#define TAM 3

int main()
{
    int matriz[TAM][TAM], i, j, soma=0;

    //lendo a matriz
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            printf("\nmatriz[%2d][%2d]: ", i, j);
            scanf("%2d", &matriz[i][j]);
        }
    }
    //imprimindo a matriz
    for(i=0; i<TAM; i++){
        printf("\n");
        for(j=0; j<TAM; j++){
            printf("%3d ", matriz[i][j]);
        }
    }

    //fazendo a soma
    for(i=0; i<TAM; i++){
        for(j=0; j<TAM; j++){
            if(i==j){
                soma = soma + matriz[i][j];
            }
        }
    }

    //imprimindo a soma
    printf("\n\nSoma dos valores da diagonal principal: %d", soma);

    return 0;
}
