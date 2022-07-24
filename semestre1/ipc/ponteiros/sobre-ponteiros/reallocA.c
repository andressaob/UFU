#include<stdio.h>
#include<stdlib.h>

int main() {
    *void realloc(void* ptr, unsigned int num);
    /*primeiro ponteiro genérico pq a função realloc não sabe o que eu vou fazer com a memória, logo ela não 
    pode me dar um ponteiro com tipo definido e posteriormente eu converto para o tipo que eu 
    quiser*/
    //segundo ponteiro genérico para poder realocar uma memória que já havia sido alocada previamente
    /*unsigned int num só pode ser um número inteiro posisitivo, pois é a quantidade de posições de 
    memória que eu quero alocar*/

    //cria vetor de 50 inteiros (200 bytes)
    int *v = (int*) malloc(200);
    //aumenta a memória alocada de 50 para 100 inteiros (400 bytes)
    v = (int*) relloc(v, 400);

    //solução

    int *v = (int*) malloc(50 * sizeof(int));
    v = (int*) realloc(v, 100 * sizeof(int));

    int *p;
    //o comando abaixo
    p = (int*) realloc(NULL, 50 * sizeof(int));
    //equivale a 
    p = (int*) malloc(50 * sizeof(int));

    //o comando abaixo
    p = (int*) realloc(p, 0);
    //equivale a
    free(p);

    int *p = (int*) malloc(5 * sizeof(int));
    int *p1 = (int*) realloc(p, 15 * sizeof(int)); //precaução para não perder a memória já alocada
    if(p1 != NULL){//realocação deu certo
        p = p1;
    }

    int *p = (int*) malloc(5 * sizeof(int));
    p = (int*) realloc(p, 15 * sizeof(int)); //sem nenhuma precaução
    if(p == NULL){//realocação deu certo
        printf("Erro: sem memória!"); //a memória/dados alocados em p foram perdidos
    }
    free(p);
}