#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char string[50], string2[50], string3[50];
    printf("Escreva o pedaço de uma frase: "); gets(string);
    printf("Escreva o resto da frase: "); fgets(string2, 20, stdin);

    strcat(string, string2); printf("\n\n%s", string);

    strcpy(string3, string); printf("\n\n%s", string3);

    printf("\n\n%d", strlen(string3));

    char busca[10], *ocorrencia=string3;
    do{
        printf("\n\nDigite a palavra que deseja buscar na frase: "); gets(busca);
        int quantidade=0; //quantidade de vezes que a palavra foi achada
        do{
            ocorrencia = strstr(ocorrencia, busca);
            if(ocorrencia != NULL){
                printf("\n\n--> %s\n", ocorrencia);
                ocorrencia++;
                quantidade++;
            }
        }while (ocorrencia != NULL);
        printf("\n\nO termo %s foi encontrado %d vezes.", busca, quantidade);
    }while (strcmp(busca, "sair") != 0);

    return 0;
}
