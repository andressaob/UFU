#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, i;
    float soma;
    soma = 0;
    printf("Digite um valor para N: "); scanf("%d", &N);

    int V[N]; //declaração do vetor depois da leitura do número N que indica o tamanho do vetor

    for (i=1;i<=N;i++) {
        printf("\nDigite um valor para V[%d]: ", i-1); scanf("%d", &V[i-1]);
        soma=soma + (i / (float)V[i-1]);

    }

    printf("\nA soma é: %.4f", soma);
    return 0;
}
