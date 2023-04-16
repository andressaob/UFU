#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char string[50], stringInvertida[50], aux;
    printf("Escreva uma palavra ou frase sem espaços: "); gets(string);

    strcpy(stringInvertida, string); //copiando a string para a string invertida

    int fim = (strlen(string))-1; //definindo a posição fim

    for(int i=0; i<(strlen(stringInvertida))/2; i++){ //arrumando a string invertida
        aux = stringInvertida[i];
        stringInvertida[i] = stringInvertida[fim-i];
        stringInvertida[fim-i] = aux;
    }

    if(string == stringInvertida){
        printf("A palavra ou frase sem espaços é um palíndromo. Original: %s. Invertida: %s.", string, stringInvertida);
    }else {
        printf("A palavra ou frase sem espaços não é um palíndromo. Original: %s. Invertida: %s.", string, stringInvertida);
    }
    //printf("%s", string); printf("\n%s", stringInvertida);

    return 0;
}
