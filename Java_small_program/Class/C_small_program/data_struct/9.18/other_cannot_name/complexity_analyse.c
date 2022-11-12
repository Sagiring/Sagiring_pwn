#include <stdio.h>
int cannot_name(int *a, int arrsize, int n)
{
    int MAXINT = 2e31 - 1;
    if (n > arrsize)
    {
        printf("error");
        return -1;
    }
    for (int i = 0; i < n; i++)
    {
        int result = 1;
        for (int cnt = 1; cnt <= i; cnt++)
        {
            result *= cnt;
            result *= 2;
        }
        if (result > MAXINT)
        {
            printf("error");
            return -1;
        }
        a[i] = result;
    }
}
int main()
{
    int n;

    int arrsize = 10;
    int name_array[arrsize];
    cannot_name(name_array, arrsize, n);
    return 0;
}
