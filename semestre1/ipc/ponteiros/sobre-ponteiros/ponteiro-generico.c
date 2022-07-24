#include <stdio.h>
#include <stdlib.h>

int main(){

    void *pp;
    int *p1, p2 = 10;

    p1 = &p2;
    pp = &p2; //ponteiro generico recebendo o endereço de uma variavel int
    printf("pp= %d\n", pp);
    pp = &p1; //ponteiro generico recebendo o endereço de ponteiro *int
    printf("pp= %d\n", pp);
    pp = p1; //ponteiro generico recebendo o endereço de uma variavel int
    printf("pp= %d\n", pp);
    /*printf("Conteúdo *pp= %d", *pp); ERRO, pois o ponteiro genérico não sabe quantas células de 
    memória precisa pegar para acessar um valor inteiro*/
    printf("Conteúdo *pp= %d", *(int*)pp); //conversão do ponteiro genérico para ponteiro inteiro

    printf("\n\n");

    void *a = 0x5DC; //1500
    printf("a = %d\n", a);
    a++; //1501
    printf("a = %d\n", a);
    a = a + 15; //1516
    printf("a = %d\n", a);
    a = a - 2; //1514
    printf("a = %d\n", a);
    /*caso o programador queira fazer operações com o ponteiro genérico e dentro dele tenha um valor 
    do tipo inteiro, double, etc., cabe ao mesmo fazer as alterações necessárias para que as operações 
    aritiméticas fiquem de acordo com o tipo*/

}