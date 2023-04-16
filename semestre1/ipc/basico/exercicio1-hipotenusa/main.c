#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int co, ca;
    float hipotenusa;

    printf("Coloque os valores do cateto oposto e do cateto adjacente, respectivamente.\n");
    scanf(" %d %d", &co, &ca);

    int quadradoCo = (co * co);
    int quadradoCa = (ca *ca);
    int somaQuadrados = (quadradoCo + quadradoCa);

    hipotenusa = sqrt(somaQuadrados);

    printf("HIPOTENUSA = %f", hipotenusa);

    return 0;
}
