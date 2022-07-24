//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int la, ca, lb, cb, i, j, k;

    printf("Digite o número de linhas e colunas, respectivamente, da matriz A: "); scanf("%d %d", &la, &ca);
    printf("\nDigite o número de linhas e colunas, respectivamente, da matriz B: "); scanf("%d %d", &lb, &cb);

    int matrizA[la][ca], matrizB[lb][cb], resultado[la][cb];

    //verificando se asa matrizes são compatíveis
    if(la!=cb){
        printf("\n\nAs dimensões das matrizes não são compatíveis. Comece de novo!");
        exit(0); //para o programa
    }
    printf("\n\n");
    //lendo matriz A
    for(i=0; i<la; i++){
        for(j=0; j<ca; j++){
            printf("matrizA[%3d][%3d]= ", i, j); scanf("%d", &matrizA[i][j]);
        }
    }
    printf("\n");
    //lendo matriz B
    for(i=0; i<lb; i++){
        for(j=0; j<cb; j++){
            printf("matrizB[%3d][%3d]= ", i, j); scanf("%d", &matrizB[i][j]);
        }
    }
    printf("\n\n");
    //imprimindo a matriz A
    for(i=0; i<la; i++){
        printf("\n");
        for(j=0; j<ca; j++){
            printf(" %3d", matrizA[i][j]);
        }
    }
    printf("\n");
    //imprimindo a matriz B
    for(i=0; i<lb; i++){
        printf("\n");
        for(j=0; j<cb; j++){
            printf(" %3d", matrizB[i][j]);
        }
    }
    printf("\n\n");
    //inicializando a matriz resultado
    for(i=0; i<la; i++){
        for(j=0; j<cb; j++){
            resultado[i][j] = 0;
        }
    }
    //calculando a matriz resultado
    for(i=0; i<la; i++){
        for(j=0; j<cb; j++){
            for(k=0; k<ca; k++){
                resultado[i][j] = resultado[i][j] + matrizA[i][k] * matrizB[k][j];
            }
        }
    }
    //imprimindo a matriz resultado
    for(i=0; i<la; i++){
        printf("\n");
        for(j=0; j<cb; j++){
            printf(" %3d", resultado[i][j]);
        }
    }

    return 0;
}
