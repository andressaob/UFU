//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include<stdio.h>
#include<stdlib.h>

int main() {
    int lA, cA, lB, cB, i, j, k;
    printf("Digite o número de linhas e colunas da matriz A, respectivamente: ");
    scanf("%d %d", &lA, &cA);
    printf("\nDigite o número de linhas e colunas da matriz B, respectivamente: ");
    scanf("%d %d", &lB, &cB);
    
    if(cA != lB){
        printf("As matrizes não são compatíveis. Comece de novo!\n");
        exit(0);
    }

    int **mA, **mB, **mResultado;
    //lendo matriz A
    //criando as linhas
    mA = (int**) malloc(lA * sizeof(int*));
    for(i=0; i<lA; i++){
        //criando as colunas
        mA[i] = (int*) malloc(cA * sizeof(int));
        for(j=0; j<cA; j++){
            printf("mA[%d][%d]= ", i, j); scanf("%d", &mA[i][j]);
        }
    }
    printf("\n\n");
    //lendo matriz B
    //criando as linhas
    mB = (int**) malloc(lB * sizeof(int*));
    for(i=0; i<lB; i++){
        //criando as colunas
        mB[i] = (int*) malloc(cB * sizeof(int));
        for(j=0; j<cB; j++){
            printf("mB[%d][%d]= ", i, j); scanf("%d", &mB[i][j]);
        }
    }
    printf("\n\n");
    //imprimindo a matriz A
    for(i=0; i<lA; i++){
        printf("\n");
        for(j=0; j<cA; j++){
            printf("%3d ", mA[i][j]);
        }
    }
    printf("\n\n");
    for(i=0; i<lB; i++){
        printf("\n");
        for(j=0; j<cB; j++){
            printf("%3d ", mB[i][j]);
        }
    }
    //inicializando a matriz resultado
    //criando as linhas
    mResultado = (int**) malloc(lA * sizeof(int*));
    for(i=0; i<lA; i++){
        //criando as colunas
        mResultado[i] = (int*) malloc(cB * sizeof(int));
        for(j=0; j<cB; j++){
            mResultado[i][j] = 0;
        }
    }
    //calculando a matriz resultando
    
    for(i=0; i<lA; i++){
        printf("\n");
        for(j=0; j<cB; j++){
            for(k=0; k<cA; k++){
                mResultado[i][j] += mA[i][k] * mB[k][j];
            }
        }
    }
    //imprimindo a matriz resultado
    for(i=0; i<lA; i++){
        printf("\n");
        for(j=0; j<cB; j++){
            printf("%3d ", mResultado[i][j]);
        }
    }
    //liberando a matriz A
    for(i=0; i<lA; i++){
        free(mA[i]);
    }
    free(mA);
    //liberando a matriz B
    for(i=0; i<lB; i++){
        free(mB[i]);
    }
    free(mB);
    //liberando a matriz resultado
    for(i=0; i<lA; i++){
        free(mResultado[i]);
    }
    free(mResultado);
}