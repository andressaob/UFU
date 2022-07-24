#include <stdio.h>
#include <stdlib.h>

int main()
{
    int **matriz = (float**) malloc(4 * sizeof(float*));
    matriz[1] = (float*) malloc(4 * sizeof(float));
    matriz[2] = (float*) malloc(4 * sizeof(float));
    matriz[3] = (float*) malloc(4 * sizeof(float));
    matriz[4] = (float*) malloc(4 * sizeof(float));
    int i, j;

    //ler matriz
    for(i=0; i<4; i++){
        for(j=0; j<4; j++){
            printf(" matriz[%d][%d]= ", i+i, j+i);
            printf("%f", &matriz[i][j]);
        }
    }
    //procurar o maior valor
    float maior = matriz[0][0];
    int localizacaoi=0, localizacaoj=0;

    for(i=0; i<4; i++){
        for(j=0; j<4; j++){
            if(maior < matriz[i][j]){
                localizacaoi = i;
                localizacaoj = j;
            }
        }
    }

    return 0;
}
