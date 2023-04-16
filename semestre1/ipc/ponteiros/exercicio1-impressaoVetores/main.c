#include <stdio.h>
#include <stdlib.h>

int main()
{
    float estatico[10];
    float *dinamico= (float*) malloc(10*sizeof(float));
    int i;

    for(i=0; i<10; i++){
        estatico[i]= 0.5*i;
        dinamico[i]= 0.5*i;
    }
    //estatico
    for(i=0; i<10; i++){
        printf("\nendereço %u conteudo %f", &estatico[i], estatico[i]);
    }
    //dinamico
    for(i=0; i<10; i++){
        printf("\nendereço %u conteudo %f", &dinamico[i], dinamico[i]);
    }
    return 0;
}
