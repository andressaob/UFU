#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char string[100];
    printf("Escreva uma frase: "); gets(string);

    int i;

    for(i=0; i < strlen(string); i++){
        string[i] = toupper(string[i]);
    }
    printf("\%s", string);


    return 0;
}
