#include<stdio.h>
#include<stdlib.h>

int main() {
    int i, *v;
    v = (int*) malloc(5 * sizeof(int));

    //lendo o vetor
    for(i=0; i<5; i++){
        printf("v[%d]= ", i); scanf("%d", &v[i]);
    }
    printf("\n\n");
    //imprimindo o vetor
    for(i=0; i<5; i++){
        printf("v[%d]= %d\n", i, (v[i] * 2));
    }
    
}