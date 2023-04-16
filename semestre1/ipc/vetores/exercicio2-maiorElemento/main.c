#include <stdio.h>
#include <limits.h>

int main()
{
    int N;

    //ler N maior que 1

    do {
        printf("Escreva um valor para N: \n"); scanf("%d", &N);
    }while (N < 1);

    int vetor[N], maior = INT_MIN;
    //int_min = atribuir o menor valor para a variável MAIOR
    //maior = 0
    for (int i = 0; i < N; i++) {
        printf("Valor: \n"); scanf("%d", &vetor[i]);
        //valor: é um valor que está dentro do vetor
        //se o tamanho for 5, então serão 5 valores

        if (vetor[i] > maior) {
            maior = vetor[i];
        }
        }
        printf("O maior valor é: %d", maior);

    return 0;
}
