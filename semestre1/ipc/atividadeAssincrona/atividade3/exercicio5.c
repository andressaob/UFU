//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    int ***cubo, i, j, k;

    srand (time(NULL));

    //criando o cubo
    //cria a profundidade
    cubo = (int***) malloc(5 * sizeof(int**));
    for(i=0; i<5; i++){
        //cria as linhas
        cubo[i] = (int**) malloc(6 * sizeof(int*));
        for(j=0; j<6; j++){
            //cria as colunas
            cubo[i][j] = (int*) malloc(7 * sizeof(int));
            for(k=0; k<7; k++){
                cubo[i][j][k] = rand() % 100 + 1;
            }
        }
    }
    //imprimindo as matrizes
    for(i=0; i<5; i++){ //define a ordem das camadas
        printf("\n\n");
        printf("\nCamada= %d", i+1);
        for(j=0; j<6; j++){
            printf("\n");
            for(k=0; k<7; k++){
                printf("%d ", cubo[i][j][k]); 
            }
        }
    }
    //liberando o cubo
    for(i=0; i<5; i++){
        for(j=0; j<6; j++){
            free(cubo[i][j]);
        }
        free(cubo[i]);
    }
    free(cubo);
}