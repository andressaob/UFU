#include <stdio.h>
#include <stdlib.h>

int main(){
    int *p = 0x5DC; //1500

    printf("p= %d\n", p);
    p++; //vai pular para a posição 1504, pois 1 valor inteiro ocupa 4 bytes de memória
    printf("p++ = %d\n", p);
    p = p + 15; //posição 1564, pois 15 valores inteiros ocupam 60 bytes de memória
    printf("p + 15 = %d\n", p);
    p = p - 2; //posição 1556, pois 2 valores inteiros ocupam 8 bytes de memória
    printf("p - 2 = %d\n", p);

    printf("\n\n");

    char *c = 0x5DC;
    int *i = 0x5DC; 
    double *d= 0x5DC;

    printf("c= %d\n", c);
    printf("i= %d\n", i);
    printf("d= %d\n", d);
    c++; //vai pular para a posição 1501, pois 1 valor caracter ocupa 1 byte de memória
    i++; //vai pular para a posição 1504, pois 1 valor inteiro ocupa 4 bytes de memória
    d++; //vai pular para a posição 1508, pois 1 valor ponto flutuante double ocupa 8 bytes de memória
    printf("c++ = %d\n", c);
    printf("i++ = %d\n", i);
    printf("d++ = %d\n", d);
    c = c + 4; //vai pular para a posição 1505, pois 4 valores caracter ocupam 4 bytes de memória
    i = i + 4; //vai pular para a posição 1520, pois 4 valores inteiro ocupam 16 bytes de memória
    d = d + 4; //vai pular para a posição 1540, pois 4 valores ponto flutuante double ocupam 32 bytes de memória
    printf("c + 4 = %d\n", c);
    printf("i + 4 = %d\n", i);
    printf("d + 4 = %d\n", d);
    c = c - 2; //vai pular para a posição 1503, pois 2 valores caracter ocupam 2 bytes de memória
    i = i - 2;//vai pular para a posição 1512, pois 2 valores inteiro ocupam 8 bytes de memória
    d = d - 2; //vai pular para a posição 1524, pois 2 valores ponto flutuante double ocupam 16 bytes de memória
    printf("c - 2 = %d\n", c);
    printf("i - 2 = %d\n", i);
    printf("d - 2 = %d\n", d);

    printf("\n\n");

    int x, y, *w, *z;
    w = &x;
    z = &y;
    if(w == z){
        printf("Os ponteiros z e w são iguais.\n");
    }else{
        printf("Os ponteiros z e w são diferentes.\n");
    }
    if(w >z){
        printf("w > z.\n");
    }else{
        printf("z < w.\n");
    }
}