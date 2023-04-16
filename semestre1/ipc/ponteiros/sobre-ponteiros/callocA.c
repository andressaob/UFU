#include<stdio.h>
#include<stdlib.h>

int main() {
    /*
    *void calloc(unsigned int num, unsigned int size);
    ponteiro genérico pq a função malloc não sabe o que eu vou fazer com a memória, logo ela não 
    pode me dar um ponteiro com tipo definido e posteriormente eu converto para o tipo que eu 
    quiser
    unsigned int num só pode ser um número inteiro posisitivo, pois é a quantidade de posições de 
    memória que eu quero alocar
    unsigned int size é o tamanho de cada posição de memória

    cria vetor de 50 inteiros (4 bytes cada)
    int *v = (int*) calloc (50, 4);
    cria vetor de 200 char (1 byte cada)
    char *c = (char*) calloc (200, 1);

    para não precisar decorar o tamanho de cada tipo, a solução é usar o sizeof

    int *v = (int*) calloc(50, sizeof(int));
    char *c = (char*) calloc(200, sizeof(char));
    */
    int *p;
    p = (int*) calloc(5, sizeof(int));
    if(p == NULL){
        printf("Erro: sem memória!\n");
        exit(1); //termina o programa
    }
    //a partir do momento que a alocação de memória deu certo, p será tratado como vetor
    int i;
    for(i=0; i<5; i++){
        printf("Digite p[%d]= ", p[i]);
        scanf("%d", &p[i]);
        //o ponteiro *p está sendo tratado como vetor
    }
    free(p); //libera a memória

    /*tanto o malloc quanto o calloc alocam a memória, mas o calloc inicializa todos os BITS do 
    espaço alocado com 0's*/
    printf("\n\n");
    int *b, *b1;
    b = (int*) malloc(5*sizeof(int));
    b1 = (int*) calloc(5, sizeof(int));
    printf("calloc \t\t malloc\n");
    for(i=0; i<5; i++){
        printf("b1[%d]= %d\n", i, b1[i]);
        printf(" b[%d]= %d\n", i, b[i]);
    }
}