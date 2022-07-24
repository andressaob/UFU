#include <stdio.h>
#include <stdlib.h>

float** aloca(int linhas, int colunas){
    float **matriz = (float**) malloc(linhas*sizeof(float*));
    for(int i=0; i<linhas;i++){
        matriz[i] = (float*) malloc(linhas*sizeof(float));
    }
    return matriz;
}
void leitura(float **matriz, int linhas, int colunas){
    for(int i=0; i<linhas;i++){
        for(int j=0; j<colunas; j++){
            printf("matriz[%d][%d]= ", i, j); scanf("%f", &matriz[i][j]);
        }
    }
    printf("\n\n");
    return;
}
float** multiplica(float **matrizA, int linhasA, int colunasA, float **matrizB, int linhasB, int colunasB){
    float **matrizProd = aloca(linhasA, colunasB);
    for(int i=0; i<linhasA; i++){
        for(int j=0; j<colunasB; j++){
            matrizProd[i][j]=0;
        }
    }
    for(int i=0; i<linhasA; i++){
        for(int j=0; j<colunasB; j++){
            for(int k=0; k<colunasA; k++){
                matrizProd[i][j]+= matrizA[i][k] * matrizB[k][j];
            }
        }
    }
    return matrizProd;
}
void imprime(float **matriz, int linhas, int colunas){
    for(int i=0; i<linhas; i++){
        printf("\n");
        for(int j=0; j<colunas; j++){
            printf(" %.1f", matriz[i][j]);
        }
    }
    printf("\n\n");
    return;
}
void desaloca(float **matriz, int linhas){
    for(int i=0; i<linhas; i++){
        free(matriz[i]);
    }
    free(matriz);
}
int main(){
    float **m1 = aloca(2, 3);
    leitura(m1, 2, 3);

    float **m2 = aloca(3,4);
    leitura(m2, 3, 4);

    float **m3 = multiplica(m1, 2, 3, m2, 3, 4);

    imprime(m1, 2, 3);
    imprime(m2, 3, 4);
    imprime(m3, 2, 4);

    desaloca(m1, 2);
    desaloca(m2, 3);
    desaloca(m3, 2);

    return 0;
}
