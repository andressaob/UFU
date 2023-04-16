#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float v1, v2, v3, v4, v5, v6, v7, v8, v9, v10;

    printf("Coloque 10 números: \n");
    scanf("%f %f %f %f %f %f %f %f %f %f", &v1, &v2, &v3, &v4, &v5, &v6, &v7, &v8, &v9, &v10);

    float media = (v1 +v2 +v3 +v4 +v5 +v6 +v7 +v8 +v9 +v10) / 10;

    printf("Média Aritmética dos 10 números colocados acima: %f \n", media);

    float DP;
    DP = sqrt( (((v1 - media) * (v1 - media)) +
                ((v2 - media) * (v2 - media)) +
                ((v3 - media) * (v3 - media)) +
                ((v4 - media) * (v4 - media)) +
                ((v5 - media) * (v5 - media)) +
                ((v6 - media) * (v6 - media)) +
                ((v7 - media) * (v7 - media)) +
                ((v9 - media) * (v9 - media)) +
                ((v10 - media) * (v10 - media))) / 10 );

    printf("O valor do Desvio Padrão dos números colocados acima é: %f \n", DP);

    return 0;
}
