#include<stdio.h>
#include<stdlib.h>

int main() {
    float ve[10], *vd;
    int i;
    vd = (float*) malloc(10 * sizeof(float));
    
    //leitura dos vetores
    for(i=0; i<10; i++){
        printf("ve[%d]= ", i); scanf("%f", &ve[i]);
    }
    printf("\n\n");
    for(i=0; i<10; i++){
        printf("vd[%d]= ", i, vd[i]); scanf("%f", &vd[i]);
    }
    printf("\n\n");
    //impressão do conteúdo dos vetores
    for(i=0; i<10; i++){
        printf("conteúdo ve[%d]= %.2f e endereço= %d\n", i, ve[i], &ve[i]); 
    }
    printf("\n\n");
    for(i=0; i<10; i++){
        printf("conteúdo vd[%d]= %.2f e endereço= %d\n", i, vd[i], &vd[i]);
    }
}