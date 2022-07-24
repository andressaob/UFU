//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include<stdio.h>
#include<stdlib.h>

int main() {
    int **matriz, i, j, diagonalP1=1, diagonalP2=1, diagonalP3=1, determinante=0;
    int diagonalS1=1, diagonalS2=1, diagonalS3=1;

    //lendo a matriz
    matriz = (int**) malloc(3 * sizeof(int*));
    for(i=0; i<3; i++){
        matriz[i] = (int*) malloc(3 * sizeof(int));
        for(j=0; j<3; j++){
            printf("matriz[%d][%d]= ", i, j); scanf("%d", &matriz[i][j]);
        }
    }
    //imprimindo a matriz
    for(i=0; i<3; i++){
        printf("\n");
        for(j=0; j<3; j++){
            printf("%d ", matriz[i][j]);
        }
    }
    //calculando a diagonal principal 1
    for(i=0; i<3; i++){
        for(j=0; j<3; j++){
            if(i == j){
                diagonalP1 *= matriz[i][j];
            }
        }
    }
    //calculando a diagonal secundária 1
    for(i=0; i<3; i++){
        for(j=0; j<3; j++){
            if(j == (3 - 1 - i)){
                diagonalS1 *= matriz[i][j];
            }
        }
    }
    //calculando as outras diagonais
    diagonalP2 = (matriz[0][1] * matriz[1][2] * matriz[2][0]);
    diagonalP3 = (matriz[0][2] * matriz[1][0] * matriz[2][1]);
    diagonalS2 = (matriz[2][1] * matriz[1][2] * matriz[0][0]);
    diagonalS3 = (matriz[2][2] * matriz[1][0] * matriz[0][1]);

    //calculando o determinante
    determinante += (diagonalP1 + diagonalP2 + diagonalP3) - (diagonalS1 + diagonalS2 + diagonalS3);

    //imprimindo o determinante
    printf("\n\nDeterminante = %d", determinante);
}