#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *vetor = (int*) malloc(5*sizeof(int)), i;

    for(i=0; i<5; i++){
        printf("vetor[%d]= ", i); scanf("%d", vetor+i);
    }
    printf("\n\n");
    for(i=0; i<5; i++){
        printf("\nvetor[%d]= %d", i, *(vetor+i));
    }


    return 0;
}
