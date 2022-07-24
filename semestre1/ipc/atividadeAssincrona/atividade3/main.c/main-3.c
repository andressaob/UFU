//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include<stdio.h>
#include<stdlib.h>

int main() {
    int **matriz, i, j, diagonalP=1, diagonalS=1, determinante=0;

    //lendo a matriz
    matriz = (int**) malloc(2 * sizeof(int*));
    for(i=0; i<2; i++){
        matriz[i] = (int*) malloc(2 * sizeof(int));
        for(j=0; j<2; j++){
            printf("matriz[%d][%d]= ", i, j); scanf("%d", &matriz[i][j]);
        }
    }
    printf("\n\n");
    //imprimindo a matriz
    for(i=0; i<2; i++){
        printf("\n");
        for(j=0; j<2; j++){
            printf("%d ", matriz[i][j]);
        }
    }
    //multiplicando a diagonal principal
    for(i=0; i<2; i++){
        for(j=0; j<2; j++){
            if(i == j){
                diagonalP = diagonalP * matriz[i][j];
            }
        }
    }
    
    //multiplicando a diagonal secundária
    for(i=0; i<2; i++){
        for(j=0; j<2; j++){
            if(j == (2 - 1 - i)){
                diagonalS = diagonalS * matriz[i][j];
            }
        }
    }
    //calculando determinante
    determinante += (diagonalP - diagonalS);
    //imprimindo o determinante
    printf("\n\nDeterminante= %d", determinante);

    for(i=0; i<2; i++){
        free(matriz[i]);
    }
    free(matriz);
}