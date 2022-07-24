//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int vetor[10], i, j;

    //lendo os valores do vetor
    for(i=0; i<10; i++) {
        printf("Coloque um valor vetor[%d]= ", i); scanf("%d", &vetor[i]);
        for(j=0; j<=i-1; j++){
            if(vetor[i] == vetor[j]){
                printf("\nDigite um número diferente.");
                i--;
            }
        }
    }
    printf("\n\nVETOR FINAL:");
    //imprimindo na tela o vetor final
    for(i=0; i<10; i++){
        printf("\nvetor[%d]= %d", i, vetor[i]);
    }

    return 0;
}
