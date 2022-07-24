//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include<stdio.h>
#include<stdlib.h>

int main(){
    float **matriz;
    int i, j;
    
    //lendo a matriz
    //criando as linhas
    matriz = (float**) malloc(3 * sizeof(float*));
    for(i=0; i<3; i++){
        //criando as colunas
        matriz[i] = (float*) malloc(3 * sizeof(float));
        for(j=0; j<3; j++){
            printf("matriz[%d][%d]= ", i, j); scanf("%f", &matriz[i][j]);
        }
    }
    printf("\n\n");
    //imprimindo a matriz
    for(i=0; i<3; i++){
        printf("\n");
        for(j=0; j<3; j++){
            printf("%.1f ", matriz[i][j]);
        }
    }
    printf("\n\n");
    float valorBusca = 1; //valor diferente de 0

    while(valorBusca != 0){
        printf("\nDigite um valor para buscar na matriz: "); scanf("%f", &valorBusca);
        for(i=0; i<3; i++){
            for(j=0; j<3; j++){
                if(valorBusca == matriz[i][j]){
                    printf("\nmatriz[%d][%d]", i, j);
                }
            }
        }
        if(valorBusca == 0){
            printf("\nIsto é tudo, pessoal!");
            //liberando a matriz resultado
            for(i=0; i<3; i++){
                free(matriz[i]);
            }
            free(matriz);
        }
    }
}
