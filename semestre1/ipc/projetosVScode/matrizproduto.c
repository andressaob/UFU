#include <stdio.h>
#include <stdlib.h>

int main()
{
    int l, c, L, C;
    //lendo o número de linhas e colunas da matriz A
    printf("Insira o número de linhas e colunas, respectivamente, da matriz A: "); scanf("%d %d", &l, &c);
    //lendo o número de linhas e colunas da matriz B
    printf("\nInsira o número de linhas e colunas, respectivamente, da matriz B: "); scanf("%d %d", &L, &C);

    int matrizA[l][c], matrizB[L][C], produtoAB[l][C], i, j, k;
    printf("\n\n");
    //lendo a matriz A
    for(i=0; i<l; i++){
        for(j=0; j<c; j++){
            printf("matrizA[%2d][%2d]= ", i, j); scanf("%d", &matrizA[i][j]);
        }
    }
    printf("\n\n");
    //lendo matriz B
    for(i=0; i<L; i++){
        for(j=0; j<C; j++){
            printf("matrizB[%d][%d]= ", i, j); scanf("%d", &matrizB[i][j]);
        }
    }
    if(l!=C){
        printf("\n\nAs matrizes fornecidas não podem ser multiplicadas. Comece tudo de novo.");
        exit(0); // para o programa
    }

    //imprimindo a matriz A
    for(i=0; i<l; i++){
        printf("\n");
        for(j=0; j<c; j++){
            printf(" %2d", matrizA[i][j]);
        }
    }
    printf("\n\n");
    //imprimindo a matriz B
    for(i=0; i<L; i++){
        printf("\n");
        for(j=0; j<C; j++){
            printf(" %2d", matrizB[i][j]);
        }
    }
    //inicializando a matriz produto
    //produtoAB[l][C] = 0;
    //calculando matriz produto
    for (i=0;i<l; i++) {
        for (j=0; j<C; j++) {
            for (k=0; k<c; k++) {
                produtoAB[l][C] = 0;
                produtoAB[i][j] = produtoAB[i][j] + matrizA[i][k] * matrizB[k][j];
            }
        }
    }
    printf("\n\n");
    //imprimindo o produto das matrizes
    for(i=0; i<l; i++){
        printf("\n");
        for(j=0; j<C; j++){
            printf(" %2d", produtoAB[i][j]);
        }
    }


    return 0;
}