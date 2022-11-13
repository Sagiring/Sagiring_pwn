#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{
    srand(10);
    for (int i = 0; i < 1000; i++)
    {
        int b = rand()%3;
        printf("%d\n", b);
    }

    return 0;
}
