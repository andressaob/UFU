#include <stdio.h>
#include <stdlib.h>

int main(){
    int x, *p;
    x = 12;
    p = &x;

    printf("x= %d", x);
    printf("\n&x= %d", &x);
    printf("\np= %d", p); //imprime o endereço da variável apontada

    printf("\n\n");
    //acessando o conteúdo do ponteiro de forma direta
    printf("x= %d", x);
    printf("\np= %d", p);
    printf("\n*p= %d", *p); //imprime o valor guardado, o valor da variável apontada
    /* o * junto à variável é usado para declarar o ponteiro e/ou para acessar o conteúdo do ponteiro, 
    ou seja, o endereço da variável armazenada e consequentemente o seu valor*/

    *p = 26; //modifica o valor da variável armazenada
    printf("\n\n");
    printf("*p= %d", *p);
    printf("\nx= %d", x);

    printf("\n\n");

    int a, *b, *b1;
    a = 10;
    b = &a;
    float c;
    c = 14;
    b1 = &c; //ERRADO, pois o tipo da variável e o tipo do ponteiro são diferentes

    printf("*b = %d", *b);
    printf("\n*b1 = %d", *b1);
    b1 = b;
    printf("\n*b1 = %d", *b1);
}
