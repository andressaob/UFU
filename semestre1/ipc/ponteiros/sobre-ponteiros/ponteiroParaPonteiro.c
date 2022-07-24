#include<stdio.h>
#include<stdlib.h>

int main(){
    int x = 10, *p = &x, **pp = &p;

    printf("pp = %d\n", pp); //endereço de p
    printf("p = %d\n", p); //endereço de x
    printf("*pp = %d\n", *pp); //conteúdo de p, que é o endereço de x
    printf("**pp = %d\n", **pp); //conteúdo de x

    printf("\n\n");

    char letra = 'a', *pchar = &letra, **ppchar = &pchar, ***pppchar = &ppchar;

    printf("letra = %c\n", letra);
    printf("*pchar = %c\n", *pchar);
    printf("**ppchar = %c\n", **ppchar);
    printf("***pppchar = %c\n", ***pppchar);
    //todos os ponteiros acima, na saída, estão apontado para o conteúdo final
}