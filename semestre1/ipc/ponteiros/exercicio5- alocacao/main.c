#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, i;
    do{
        printf("Digite um valor para N: "); scanf("%d", &N);
    }while (N<=0);

    int *vetor= (int*) malloc(N*sizeof(int));

    for(i=0; i<N; i++){
        do{
            printf("\nvetor[%d]= ", i); scanf("%d", &vetor[i]);
        }while (vetor[i] < 2);
    }
    printf("\n\n");
    for(i=0; i<N; i++){
        printf("\nvetor[%d]= %d", i, vetor[i]);
    }

    free(vetor);


    return 0;
}
