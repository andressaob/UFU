//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int N, i;
    float media=0, dp=0;
    //lendo N
    printf("Digite um valor para N: "); scanf("%d", &N);
    //armazenando N no vetor
    int vetor[N];

    //lendo N valores do vetor
    for(i=1; i<=N; i++){
        printf("\nvetor[%d]= ", i-1); scanf("%d", &vetor[i-1]);
        //cálculo inicial da média
        media= media + vetor[i-1];
    }
    //cálculo final da média
    media=media/N;


    for(i=0; i<N; i++){
        //cálculo inicial do dp
        dp= dp + (media-vetor[i])*(media-vetor[i]);
    }
    dp=dp/(float)N;
    //cálculo final do dp
    dp=sqrt(dp);

    //impressão na tela da média e dp
    printf("Média= %.2f e desvio padrão= %.2f", media, dp);

    return 0;
}
