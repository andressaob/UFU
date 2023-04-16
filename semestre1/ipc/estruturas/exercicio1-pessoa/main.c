#include <stdio.h>
#include <stdlib.h>

struct pessoa {
    char nome[50];
    int idade;
    char endereco[100];
};
int main(){
    struct pessoa p1;
    printf("Nome P1: "); gets(p1.nome); setbuf(stdin, NULL); //sempre colocar isso para não dar problema na memória
    printf("\nIdade P1: "); scanf("%d", &p1.idade); setbuf(stdin, NULL);
    printf("\nEndereço residencial P1: "); gets(p1.endereco); setbuf(stdin, NULL);
    printf("\n\n");
    printf("\nNome P1: %s, idade P1: %d e endereço P1: %s.", p1.nome, p1.idade, p1.endereco);

    printf("\n\n");
    struct pessoa *p2 = (struct pessoa *) malloc(sizeof(struct pessoa));
    printf("Nome P2: "); gets(p2->nome); setbuf(stdin, NULL);
    printf("\nIdade P2: "); scanf("%d", &p2->idade); setbuf(stdin, NULL);
    printf("\nEndereço residencial P2: "); gets(p2->endereco); setbuf(stdin, NULL);
    printf("\n\n");
    printf("\nNome P2: %s, idade P2: %d e endereço P2: %s.", p2->nome, p2->idade, p2->endereco);
    free(p2);
    return 0;

}
