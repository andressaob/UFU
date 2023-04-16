#include<stdio.h>
#include<stdlib.h>

int main() {
    /*
    ponteiro (1 nível): cria um vetor
    int *p = (int*) malloc(5 * sizeof(int));
    ponteiro para ponteiro (2 níveis): cria uma matriz
    int **m;
    ponteiro para ponteiro para ponteiro (3 níveis): cria um cubo, 3 dimensões
    int ***c;

    em um ponteiro para ponteiro, cada nível do ponteiro permite criar uma nova dimensão no vetor */

    int **p; //2 "*" = 2 níveis = 2 dimensões
    int i, j, N = 2;
    
    //criar um vetor de ponteiros (int*)
    p = (int**) malloc(N * sizeof(int*));
    //cria as linhas da matriz
    for(i=0; i<N; i++){
        //criar um vetor de inteiros
        p[i] = (int*) malloc(N * sizeof(int));
        //cria as colunas da matriz
        for(j=0; j<N; j++){
            //lê a matriz de inteiros
            scanf("%d", &p[i][j]);
        }
    }
    //liberando a matriz
    for(i=0; i<N; i++){
        free(p[i]);
    }
    free(p);
}