#include <stdio.h>
#include <stdlib.h>

int main(){

    int lNotas=10, cNotas=3, i, j, maior=0, contador=0;
    float notas[lNotas][cNotas];

    //lendo as notas na matriz
    for(i=1; i<=lNotas; i++){
        for(j=1; j<=cNotas; j++){
            printf("Notas[%d][%d]= ", i, j); scanf("%.2f", &notas[i][j]);
        }
    }
    printf("\n\n");

    //maior nota dentre todas as provas e quantos alunos a obtiveram
    for(i=1; i<=lNotas; i++){
        for(j=1; j<=cNotas; j++){
            if(notas[i][j]>maior){
                maior = matriz[i][j];
                contador = 1;
            }else if(notas[i][j]==maior){
                contador++;
            }
        }
    }

    return 0;
}
