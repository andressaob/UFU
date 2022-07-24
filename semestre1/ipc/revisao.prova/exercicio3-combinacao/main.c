#include <stdio.h>
#include <stdlib.h>

long long int fatorial(int a){
    if (a==0)
        return 1;
    else
        return a * fatorial(a-1);
}

long long int combinacao(int x, int y){
    return fatorial(x) / (fatorial(y) * fatorial(x-y));
}
int main(){
    int n, s;
    long long int comb;
    printf("Digite um valor para N: "); scanf("%d", &n);
    printf("Digite um valor para S: "); scanf("%d", &s);

    comb = combinacao(n, s);

    printf("Combinação de N e S: %lld", comb);
}
