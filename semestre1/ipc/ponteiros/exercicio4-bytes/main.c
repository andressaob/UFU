#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("\nchar= %d bytes", sizeof(char));
    printf("\nint= %d bytes", sizeof(int));
    printf("\nfloat= %d bytes", sizeof(float));
    printf("\ndouble= %d bytes", sizeof(double));
    printf("\nlong double= %d bytes", sizeof(long double));
    printf("\nlong= %d bytes", sizeof(long));
    printf("\nlong long= %d bytes", sizeof(long long));
    printf("\nshort= %d bytes", sizeof(short));
    printf("\nlong int= %d bytes", sizeof(long int));

    //independente do tipo da variável e da quantidade de apontamentos, o ponteiro sempre terá 8 bytes
    printf("\n\nchar* = %d bytes", sizeof(char*));
    printf("\nint** = %d bytes", sizeof(int**));
    printf("\nshort*** = %d bytes", sizeof(short***));

    return 0;
}
