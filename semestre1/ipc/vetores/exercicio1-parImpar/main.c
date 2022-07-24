#include <stdio.h>
#include <stdlib.h>

int main()
{
    int vetor[9], i, par, impar;

    for (i=0; i<=9; i++) {
        printf("Coloque um valor para a posicao: [%d]: ", i); scanf("%d", &vetor[i]);
        //atribuindo valor para as posições do vetor
        if (vetor[i]%2==0) {
            printf("O número %d é par.\n", vetor[i]);
        }else {
            printf("O número %d é ímpar.\n", vetor[i]);
        } //o if vai passar em cada valor lido e vai validar se é ímpar ou par e irá para o próximo valor
    }


    return 0;
}
