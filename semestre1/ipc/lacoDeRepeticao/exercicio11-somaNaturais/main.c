#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, soma=0;

    printf("A soma dos múltiplos de 3 ou 5 menores que 1000 é: ");

    for (i=0; i<1000; i++) {
        if(i%3==0 || i%5==0) {
            soma= soma + i;
        }
    }
    printf("%d ", soma);

    return 0;
}
