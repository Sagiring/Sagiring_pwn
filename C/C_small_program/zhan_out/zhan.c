#include <stdio.h>

int main()
{
    char buffer[12];
    int v6 = 0;
    int v7 = 0;
    int v8 = 0;

    scanf("%d", &v6);
  
    if (v7 == 0)
    {
        printf("Try again\n");
        printf("v6 = %d", v6);
    }
    else
    {
        printf("You have success\n");
        printf("%d %d", v7, v8);
    }
    return 0;
}