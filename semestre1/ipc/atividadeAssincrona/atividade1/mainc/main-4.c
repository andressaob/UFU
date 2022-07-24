//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, i;
    float soma=0;
    //lendo N
    printf("Digite um número para N: "); scanf("%d", &N);
    //armazenando N no vetor
    int vetor[N];

    //lendo os N valores do vetor
    for(i=1; i<=N; i++){
        printf("\nvetor[%d]= ", i-1); scanf("%d", &vetor[i-1]);
        //calculando a soma
        soma= soma + (i/(float)vetor[i-1]);
    }
    //imprimindo a soma
    printf("\nSoma= %.4f", soma);

    return 0;
}
