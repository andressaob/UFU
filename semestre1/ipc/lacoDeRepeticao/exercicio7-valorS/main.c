#include <stdio.h>
#include <stdlib.h>

int main()
{
    int numerador, denominador;
    float soma;
    numerador = 1;
    denominador = 1;
    soma = 0;

    while (denominador <= 50) {
        printf("%d/%d\n", (numerador), (denominador));
        soma = soma + (numerador) / (denominador);

        denominador++;
        numerador=numerador + 2;
    }
    printf("S= %.2f", soma);



    return 0;
}

//não pode ser um for dentro do while pq a cada denominador, ele vai fazer 99 vezes a contagem.
//numerador = numerador+2 e denominador= denominador+1

/*int numerador, denominador, soma;
    denominador = 1;
    soma = 0;

    while (denominador <= 50) {
        for (numerador=1; numerador<=99; numerador=numerador+2) {
            soma=soma + (numerador/denominador);
            printf("%d/%d\n", numerador, denominador);
        }
        printf("-----------------------------------------------------\n");
        denominador++;
    }*/
