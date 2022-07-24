//Nome: Andressa Oliveira Bernardes
//Matrícula: 12121BSI201

#include <stdio.h>
#include <stdlib.h>

int main()
{
    //lendo tipo de grãos
    char tipo;
    printf("Digite o tipo de grão entre os tipos A, B, C e D: "); scanf("%c", &tipo);
    if(tipo != 'A' && tipo != 'a' && tipo != 'B' && tipo != 'b' && tipo != 'C' && tipo != 'c' && tipo != 'D' &&
    tipo != 'd') {
        printf("Tipo não reconhecido.");
        exit(0); //para o programa
    }

    //lendo quantidade de quebrados
    int quebrados;
    printf("Digite a quantidade de grãos quebrados, entre 3, 4 e 5: "); scanf("%d", &quebrados);

    //definindo preços
    float precoA3=170.00, precoA4=151.30, precoA5=139.20, precoB3=153.00, precoB4=136.17, precoB5=125.28,
    precoC3=139.23, precoC4=123.91, precoC5=112.76, precoD3=128.09, precoD4=117.84, precoD5=104.88;

    //validando através do tipo e da quantidade de quebrados qual será o preço da saca
    if(tipo == 'A'|| tipo == 'a'){
        if(quebrados == 3) {
            printf("Preço por saca: R$%.2f", precoA3);
        }else if(quebrados == 4) {
            printf("Preço por saca: R$%.2f", precoA4);
        }else if(quebrados == 5) {
            printf("Preço por saca: R$%.2f", precoA5);
        }else {
            printf("Não tem essa quantidade de grãos quebrados");
        }
    }else if(tipo == 'B'|| tipo == 'b'){
        if(quebrados == 3) {
            printf("Preço por saca: R$%.2f", precoB3);
        }else if(quebrados == 4) {
            printf("Preço por saca: R$%.2f", precoB4);
        }else if(quebrados == 5) {
            printf("Preço por saca: R$%.2f", precoB5);
        }else {
            printf("Não tem essa quantidade de grãos quebrados");
        }
    }else if(tipo == 'C' || tipo == 'C'){
        if(quebrados == 3) {
            printf("Preço por saca: R$%.2f", precoC3);
        }else if(quebrados == 4) {
            printf("Preço por saca: R$%.2f", precoC4);
        }else if(quebrados == 5) {
            printf("Preço por saca: R$%.2f", precoC5);
        }else {
            printf("Não tem essa quantidade de grãos quebrados");
        }
    }else {
        if(quebrados == 3) {
            printf("Preço por saca: R$%.2f", precoD3);
        }else if(quebrados == 4) {
            printf("Preço por saca: R$%.2f", precoD4);
        }else if(quebrados == 5) {
            printf("Preço por saca: R$%.2f", precoD5);
        }else {
            printf("Não tem essa quantidade de grãos quebrados.");
        }
    }

    return 0;
}
