#include<stdio.h>
#include<stdlib.h>

int main() {
    printf("char= %d byte\n", sizeof(char));
    printf("int= %d bytes\n", sizeof(int));
    printf("float= %d bytes\n", sizeof(float));
    printf("duble= %d bytes\n", sizeof(double));
    printf("long double= %d bytes\n", sizeof(long double));
    printf("\n\n");
    printf("char*= %d bytes, char**= %d e char***= %d bytes\n", sizeof(char*), sizeof(char**), 
    sizeof(char***));
    printf("int*= %d bytes, int**= %d e int***= %d bytes\n", sizeof(int*), sizeof(int**), 
    sizeof(int***));
    printf("float*= %d bytes, float**= %d e float***= %d bytes\n", sizeof(float*), sizeof(float**), 
    sizeof(float***));
    printf("double*= %d bytes, double**= %d e double***= %d bytes\n", sizeof(double*), sizeof(double**), 
    sizeof(double***));
    printf("long double*= %d bytes, long double**= %d e long double***= %d bytes\n", 
    sizeof(long double*), sizeof(long double**), sizeof(long double***));

}