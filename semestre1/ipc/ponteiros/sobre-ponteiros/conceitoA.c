#include<stdio.h>
#include<stdlib.h>

int main(){
    int x= sizeof (int);

    printf("x = %d\n", x);
    printf("char: %d\n", sizeof(char));
    printf("int: %d\n", sizeof(int));
    printf("float: %d\n", sizeof(float));
    printf("double: %d\n", sizeof(double));
}