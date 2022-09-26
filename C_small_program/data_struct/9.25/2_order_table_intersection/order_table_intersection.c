#include <stdio.h>
#include <stdlib.h>
typedef struct
{
    int *elem;
    int length;
} va;

void table_sort(va a)
{
    int cnt = 0;
    for (int i = 0; i < a.length; i++)
    {
        if (a.elem[i] == -1)
        {
            for (int cnt = i; cnt < a.length; cnt++)
            {
                a.elem[cnt] = a.elem[cnt + 1];
            }
            a.elem[a.length - 1] = -1;
            a.length--;
        }
    }
}

void table_delete(va a, int aloc)
{

    if (aloc < a.length)
    {
        a.elem[aloc] = -1;
    }
}

void table_intersection(va a, va b)
{
    int aloc = 0;
    int bloc = 0;
    while (1)
    {
        if (aloc == a.length )
        {
            break;
        }
        if (a.elem[aloc] == b.elem[bloc])
        {
            aloc++;
            bloc = 0;
        }
        else if (a.elem[aloc] < b.elem[bloc])
        {
            table_delete(a, aloc);
            bloc = 0;
            aloc++;
        }
        else
        {
            if (bloc == b.length - 1)
            {
                table_delete(a, aloc);
                aloc++;
                bloc = 0;
            }
            else
            {
                bloc++;
            }
        }
    }
}

int main()
{
    va a;
    a.length = 11;
    a.elem = (int *)malloc(sizeof(int) * a.length);
    for (int i = 0; i < a.length; i++)
    {
        a.elem[i] = i + 1;
    }
    printf("a = ");
    for (int i = 0; i < a.length; i++)
    {
        printf("%d ", a.elem[i]);
    }
    printf("\n");
    // a[] = {1,2,3,4,5,6}
    va b;
    b.length = 10;
    b.elem = (int *)malloc(sizeof(int) * a.length);
    for (int i = 0; i < b.length; i++)
    {
        b.elem[i] = 2 * i;
    }
    printf("b = ");
    for (int i = 0; i < b.length; i++)
    {
        printf("%d ", b.elem[i]);
    }
    printf("\n");
    // b[] = {0,2,4,6,8}

    table_intersection(a, b);
    table_sort(a);

    printf("a = ");
    for (int i = 0; i < a.length; i++)
    {
        printf("%d ", a.elem[i]);
    }

    free(a.elem);
    free(b.elem);
    return 0;
}