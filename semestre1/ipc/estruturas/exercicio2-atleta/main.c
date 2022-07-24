#include <stdio.h>
#include <stdlib.h>

struct atleta{
    char nome[50]; char esporte[20]; int idade; float peso; float altura;
};
int main(){
    struct atleta a[5];
    int i, maiorAlt, maisVelho, posicaoV, posicaoA;

    maiorAlt = 1; maisVelho = 1;
    for(i=0; i<5; i++){
        printf("Digite um nome para o atleta: "); gets(a[i].nome); setbuf(stdin,NULL);
        printf("\nDigite qual esporte esse atleta pratica: "); gets(a[i].esporte); setbuf(stdin,NULL);
        printf("\nDigite a idade desse atleta: "); scanf("%d", &a[i].idade); setbuf(stdin,NULL);
        printf("\nDigite o peso desse atleta: "); scanf("%f", &a[i].peso); setbuf(stdin,NULL);
        printf("\nDigite a altura desse atleta: "); scanf("%f", &a[i].altura); setbuf(stdin,NULL);
        printf("\n\n");
        if(a[i].altura > maiorAlt) {
            maiorAlt = a[i].altura;
            posicaoA = i;
        }
        if(a[i].idade > maisVelho){
            maisVelho = a[i].idade;
            posicaoV = i;
        }
    }
    printf("O %s é o atleta mais velho, com %d anos e o mais alto é o %s, com %.2f de altura.", a[posicaoV].nome,
    a[posicaoV].idade, a[posicaoA].nome, a[posicaoA].altura);
    return 0;
}
