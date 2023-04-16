#include <stdio.h>
#include <stdlib.h>
#define pi 3.141592

float volume (float raio, float altura){
    return pi * (raio*raio) * altura;
}
int main(){
    float r, h, vol;
    printf("Digite um valor para o raio: "); scanf("%f", &r);
    printf("Digite um valor para a altura do cilindro: "); scanf("%f", &h);

    vol = volume(r, h);
    printf("Volume: %.6f", vol);
}
