#include <stdio.h>
#include <stdlib.h>
#include<string.h>

int main()
{
    char string[50], aux;
    printf("Digite uma palavra ou frase: "); gets(string);

    int i, fim = (strlen(string))-1;

    for(i=0; i<(strlen(string))/2; i++){
        //trocando os valores de posição
        aux = string[i];
        string[i] = string[fim-i];
        string[fim-i] = aux;
    }

    printf("%s", string); //imprimindo a string ao contrário

    return 0;
}
