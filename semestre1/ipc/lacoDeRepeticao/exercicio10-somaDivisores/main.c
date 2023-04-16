#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, i, soma=0;

    printf("Digite um número inteiro positivo: ", num); scanf("%d", &num);
    printf("A soma dos divisores é: ");

    for (i=1; i<num; i++) {
        if (num%i == 0) {
            soma=soma + i;
        }
    }
    printf("%d ", soma);
    return 0;
}
