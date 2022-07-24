#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int N, i;
    float media=0, dp=0;
    printf("Digite um valor para N: "); scanf("%d", &N);
    int vetor[N];

    for(i=1; i<=N; i++){
        printf("\nvetor[%d]= ", i-1); scanf("%d", &vetor[i-1]);
        media= media + vetor[i-1];
    }
    media=media/N;

    for(i=0; i<N; i++){
        dp= dp + (media-vetor[i])*(media-vetor[i]);
    }
    dp=dp/(float)N;
    dp=sqrt(dp);

    printf("Média= %.2f e desvio padrão= %.2f", media, dp);

    return 0;
}
