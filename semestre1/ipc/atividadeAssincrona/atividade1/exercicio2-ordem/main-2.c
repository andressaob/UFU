#include <stdio.h>
#include <stdlib.h>

int main()
{
    int vetor[10], i, j;

    for(i=0; i<10; i++) {
        printf("Coloque um valor para vetor[%d]= ", i); scanf("%d", &vetor[i]);
        for(j=0; j<=i-1; j++){
            if(vetor[i] == vetor[j]){
                printf("\nDigite um número diferente.");
                i--;
            }
        }
    }

    return 0;
}
