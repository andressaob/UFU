#include<stdio.h>
#include<stdlib.h>

int main() {
    /*
    void* malloc(unsigned int num);
    unsigned int num só pode ser um número inteiro posisitivo, pois é a quantidade de posições de 
    memória que eu quero alocar

    ponteiro genérico pq a função malloc não sabe o que eu vou fazer com a memória, logo ela não 
    pode me dar um ponteiro com tipo definido e posteriormente eu converto para o tipo que eu 
    quiser
    
    cria vetor de 50 inteiros (200 bytes)
    int *d = malloc(200);
    cria vetor de 200 char (200 bytes)
    char *c = malloc(200);
    na alocação da memória, deve-se levar em conta o tamanho do tipo

    vetor de tamanho 50
    int *d = (int*) malloc(200);
    char *c = (char*) malloc(50);
    
    para não precisar saber de cor quantos bytes cada tipo usa, a solução é colocar sizeof
    
    int *d = (int*) malloc(50 * sizeof(int));
    char *c =  (char*) malloc(50 * sizeof(char));

    o (*int) força o ponteiro que era genérico a virar inteiro, converte

    */
    //se não houver memória suficiente para alocar a memória requisitada, a função malloc retorna NULL
    int *p;
    p = (int*) malloc(5 * sizeof(int));
    if(p == NULL){
        printf("Erro: sem memória!\n");
        exit(1); //termina o programa
    }
    //a partir do momento que a alocação de memória deu certo, p será tratado como vetor
    int i;
    for(i=0; i<5; i++) {
        printf("Digite p[%d]: ", p[i]);
        scanf("%d", &p[i]);
        //o ponteiro *p está sendo tratado como vetor
    }
    free(p);
    //libera a memória alocada
}
