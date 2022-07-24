#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, menor, maior, i;
    float media;
    menor = 999999999;
    maior = 0;
    media = 0;

    for (i = 1; i <= 10; i++) {
        printf("Digite um número:\n");
        scanf("%d", &num);
        if (num >= 0) {
            if (num < menor)
                menor = num;
            if (num > maior)
                maior = num;
        }else {
            printf("Só são aceitos números positivos!\n");
            i--; // caso insira um número negativo (por exemplo, numero 4), volta para o anterior e pede para digitar de novo
        }
        media = media + num;
    }
   media = media/10.0;
    printf("O menor número é: %d\n", menor);
    printf("O maior número é: %d\n", maior);
    printf("A média é: %.2f\n", media);

    return 0;
}
