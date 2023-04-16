#include<stdio.h>
#include<stdlib.h>

int main(){
    int vetor[5] = {1, 2, 3, 4, 5}, i;
    int *p  = vetor; //*p é equivalente ao vetor, pois o vetor é uma espécie de ponteiro

    for(i=0; i<5; i++){
        printf("%d\n", *(p+i)); /* *(p+i)=*p[i], p+i pq vai pegar o endereço para o qual o vetor está 
        apontando e somar a i posições de memória*/
    }

    int *vet[2]; //vetor de 2 ponteiros, cada ponteiro vai apontar para um lugar diferente na memória
    int x = 2, y[2] = {20, 30};

    vet[0] = &x;
    vet[1] = y; //onde começa o vetor y

    printf("\n\n");

    printf("vet[0]= %p\n", vet[0]); //vai imprimir &x; %p é para imprimir o ponteiro
    printf("vet[1]= %p\n", vet[1]); //vai imprimir o &y[0]

    printf("\n\n");

    printf("*vet[0]= %d\n", *vet[0]); //vai imprimir o conteúdo de x
    printf("*vet[1]= %d\n", *vet[1]); //vai imprimir o conteúdo de y

}