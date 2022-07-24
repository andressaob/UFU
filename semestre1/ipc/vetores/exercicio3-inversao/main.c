#include <stdio.h>
#include <stdlib.h>

#define TAM 20

int main()
{
    int A[TAM], B[TAM], i, aux, fim=TAM-1;//fim = última posição do vetor

    for (i=0; i<TAM; i++) {
        printf("Valor A[%d]: ", i); scanf("%d", &A[i]);
    } //lendo valores do vetor A

    printf("\nVetor A: ");
    for (i=0; i<TAM; i++) {
         printf("%d ", A[i]);
    }//imprimindo o vetor A

    for(i=0;i<TAM;i++) {
        B[i]=A[i];
    }
    /**
    for(i=0;i<TAM;i++) {
        B[i]=A[fim];
        fim--;
    }//passando os valores de A para B*/ //sugestão do matheus, para não ter que criar todos os valores de A para B e fazer o for para trocar os elementos de posição

    for(i=0; i<TAM/2;i++) { //a<10 pois vamos trocar apenas até o décimo elemento, pois o restante já estará trocado
        aux = B[i];
        B[i] = B[fim];
        B[fim] = aux;
        fim--;//decremento pois depois que validar com a última posição, irá validar com a penúltima e assim por diante
    }//trocando os valores das posições

    printf("\nVetor B: ");
    for (i=0; i<TAM; i++) {
         printf("%d ", B[i]);
    }//imprimindo o vetor B

    return 0;
}












/*int A[TAM], B[TAM], i, contador=0;

    for (i=0; i<TAM; i++) {
        printf("Valor A[%d]: ", i); scanf("%d", &A[i]);
    }
    for (i=TAM-1; i>=0; i--) {
        B[contador]=A[i];
        contador++;
    }
    for (i=0; i<TAM; i++) {
        printf("vetorA: %d vetorB: %d\n", A[i], B[i]);
    }*/
