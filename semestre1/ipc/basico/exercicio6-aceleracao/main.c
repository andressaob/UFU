#include <stdio.h>
#include <stdlib.h>

int main()
{
    float vInicial, vFinal, intervaloTempo;

    printf("Coloque o valor da velocidade inicial: \n");
    scanf("%f", &vInicial);

    printf("Coloque o valor da velocidade final: \n");
    scanf("%f", &vFinal);

    printf("Coloque o valor do intervalo de tempo: \n");
    scanf("%f", &intervaloTempo);

    printf("O valor da ACELERAÇÃO MÉDIA é: %f\n", (vFinal - vInicial) / intervaloTempo);

    return 0;
}
