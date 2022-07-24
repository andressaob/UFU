#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAM 1000

void ordena(int *vetor){ //função para ordenação do valor
    for(int i=0; i<TAM-1; i++){ //analisando posição por posição
        for(int j=i+1; j<TAM; j++){
            if(vetor[i] > vetor[j]){ //realizando a troca
                int aux = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = aux;
            }
        }
    }

    return;
}

int sequencial(int busca, int *vetor, int tamanho, int *comparacoes){
    for(int i=0; i < TAM; i++){
        (*comparacoes)++;
        if(vetor[i] == busca)
            return i; //retorna a posicao do valor
        else if(vetor[i] > busca)
            return -1; // -1 caso não encontre
    }
}

int main()
{
    int *vetor, ordenacao, i, busca;
    //alocando o vetor dinâmicamente
    vetor = (int*) malloc(TAM * sizeof(int));
    //função para atribuir valores aleatórios para sas posições do valor
    srand(time(NULL));
    //atribuindo números aleatórios para as posições do vetor
    for(i=0; i<TAM; i++){
        vetor[i] =  rand() % 500000 - 1;
    }
    //ordenando o vetor
    ordena(vetor);
    for(i=0; i<TAM;i++){
        printf(" %d", vetor[i]);
    }

    do {
        printf("\n\nDigite um número para fazer a busca sequencial (digite 0 para sair): ");
        scanf("%d", &busca);

        int posicaoSequencial, comparacoesS, posicaoBiIterativa, comparacoesBI, posicaoBiRecursiva, comparacoesBR;
        //busca sequencial
        sequencial(busca, vetor, TAM, comparacoesS);
        printf("\nposição %d, com %d comparações.", posicaoSequencial, comparacoesS);
        //busca binária iterativa
        //printf("\nposição %d, com %d comparações.", posicaoBiIterativa, comparacoesBI);
        //busca binaria recursiva
        //printf("\nposição %d, com %d comparações.", posicaoBiRecursiva, comparacoesBR);
        }while (busca != 0);

        return 0;
}
