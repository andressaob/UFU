#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, c;

    printf("Escreva o valor para A.\n");
    scanf(" %d",&a);
    printf("Escreva o valor para B.\n");
    scanf(" %d",&b);
    printf("Escreva o valor para C.\n");
    scanf(" %d",&c);

    if ((c > b) && (b > a)){
        printf("Em ordem: %d %d %d.\n", a, b, c); //ok
    }else if ((c > a) && (b > c)){
        printf("Em ordem: %d %d %d.\n", a, c, b); //ok
    }else if ((b > a) && (a > c)){
        printf("Em ordem: %d %d %d.\n", c, a, b); //ok
    }else if ((c > a) && (a > b)) {
        printf("Em ordem: %d %d %d.\n", b, a, c); //ok
    }else if ((a > c) && (c > b)) {
        printf("Em ordem: %d %d %d.\n", b, c, a); // ok
    }else {
        printf("Em ordem: %d %d %d.\n", c, b, a); //ok
    }

    return 0;
}
