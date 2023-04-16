#include <stdio.h>
#include <stdlib.h>

int main()
{
    int numero;

    printf("Escreva um número inteiro qualquer: \n");
    scanf("%d", &numero);

    if (numero % 2 == 0) {
        printf("Esse número é par.");
    }else
        printf("Esse número é ímpar.");

    return 0;
}
