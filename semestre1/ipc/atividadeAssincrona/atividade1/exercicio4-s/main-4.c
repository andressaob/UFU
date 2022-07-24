#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, i;
    float soma=0;
    printf("Digite um número para N: "); scanf("%d", &N);
    int vetor[N];

    for(i=1; i<=N; i++){
        printf("\nvetor[%d]= ", i-1); scanf("%d", &vetor[i-1]);
        soma= soma + (i/(float)vetor[i-1]);
    }
    printf("\nSoma= %.4f", soma);

    return 0;
}
