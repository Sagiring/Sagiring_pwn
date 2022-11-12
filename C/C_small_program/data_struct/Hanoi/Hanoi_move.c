#include <stdio.h>
int c = 1;

void move(char x, int n, char z)
{
    printf("%i>搬动盘子%i>从%c->%c \n", c++, n, x, z);
}
void hanoi(int n, char x, char y, char z)
{
    if (n == 1)
    {
        move(x, 1, z);
    }
    else
    {
        hanoi(n - 1, x, z, y);
        move(x, n, z);
        hanoi(n - 1, y, x, z);
    }
}

int main(int argc, char const *argv[])
{
    char x, y, z;
    x = 'A';
    y = 'B';
    z = 'C';
    int n = 5 ;
    hanoi(n, x, y, z);
    return 0;
}
