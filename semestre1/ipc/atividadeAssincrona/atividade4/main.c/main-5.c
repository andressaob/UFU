//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201

#include <stdio.h>
#include <stdlib.h>

long long int fibonacciIterativo(int n){
    long long int atual, ultimo=1, penultimo=0;
    for (int i=1; i<=n; i++){
        atual = penultimo + ultimo;
        ultimo = penultimo;
        penultimo = atual;
    }
    return atual;
}
int fibonacciRecursivo(int n){
    if(n==0 || n==1)
        return n;
    else
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2);
}
int main(){
    int i;
    for(i=1; i<100; i++){
        printf("\n termo %d: %lld", i, fibonacciIterativo(i));
    } //o tempo de execução do fibonacci iterativo é de 0.002s
    for(i=1; i<100; i++){
        printf("\n termo %d: %d", i, fibonacciRecursivo (i));
    } //o tempo de execução do fibonacci recursivo é superior 1 min
    return 0;
}

