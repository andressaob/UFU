#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float potenciacao(int n){
    if(n==1)
        return 1;
    else
        return pow(n, n) + potenciacao(n-1);
}
int main(){
    int N, soma;

    printf("Digite um número para N: "); scanf("%d", &N);

    soma = potenciacao(N);
    printf("Soma= %d", soma);
    return 0;
}
