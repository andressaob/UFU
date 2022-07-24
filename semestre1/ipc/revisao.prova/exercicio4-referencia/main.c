#include <stdio.h>
#include <stdlib.h>
#define pi 3.141592

void separa(float valor, int *inteiro, float *fracionario){
    *inteiro = (int) valor;
    *fracionario = valor - *inteiro;
}
int main(){
    float fracionario;
    int inteiro;
    separa(pi, &inteiro, &fracionario);
    printf("Valor: %.6f, parte inteira: %d e parte decimal: %.6f.", pi, inteiro, fracionario);
}
