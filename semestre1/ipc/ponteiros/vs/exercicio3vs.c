#include<stdio.h>
#include<stdlib.h>

int main() {
    float a, *b, **c, ***d;
    printf("Digite um valor para 'a': "); scanf("%f", &a);
    b = &a; //dobro
    c = &b; //triplo
    d = &c; //quádruplo

    printf("\na= %.2f, *b= %.2f, **c= %.2f e ***d= %.2f", a, *b * 2, **c * 3, ***d * 4);
}