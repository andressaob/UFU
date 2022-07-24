#include <stdio.h>
#include <stdlib.h>

int crescente(int n){
	if(n == -1) { //-1 pq é para printar o 0 também
		return; //return 0;
	}
	crescente(n-1); //função primeiro (n-1) pq é para começar do menor número
	printf("%d ", n); //depois o print n, que é o último número
}
int decrescente(int n){
    if(n == -1) {
		return; //return 0;
	}
	printf("%d ", n); // primeiro o print n, que é o maior número
	decrescente(n-1); //depois a função (n-1), pq é para terminar no menor número
}
int main(){
    int N;
    printf("Digite um número para N: "); scanf("%d", &N);

    printf("\n crescente: "); crescente(N);
    printf("\n decrescente: "); decrescente(N);
    return 0;
}
