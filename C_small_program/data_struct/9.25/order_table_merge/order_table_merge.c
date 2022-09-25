#include <stdio.h>
#include <stdlib.h>
typedef struct
{
    int *elem;
    int length;
} va;

void table_sort(va va, int x, int loc)
{
    for (int i = va.length - 1; i > loc; i--)
    {
        va.elem[i] = va.elem[i - 1];
    }
    va.elem[loc] = x;
}

int table_insert(va va, int x)
{
    int loc;
    va.length += 1;
    va.elem = realloc(va.elem, sizeof(int) * (va.length));
    if (x <= va.elem[0])
    {
        loc = 0;
        table_sort(va, x, loc);
        return 1;
    }
    else if (x >= va.elem[va.length - 2])
    {
        loc = va.length - 1;
        table_sort(va, x, loc);
        return 1;
    }
    for (int i = 1; i < va.length - 2; i++)
    {

        if (x <= va.elem[i])
        {
            loc = i;
            table_sort(va, x, loc);
            return 1;
        }
    }
    return -1;
}

int table_equal(va a, int x)
{
    for (int i = 0; i < a.length; i++)
    {
        if (a.elem[i] == x)
        {
            return 1;
        }
    }
    return 0;
}

int main()
{
    va a;
    a.length = 6;
    a.elem = (int *)malloc(sizeof(int) * a.length);
    for (int i = 0; i < a.length; i++)
    {
        a.elem[i] = i + 1;
    }
    printf("a= ");
    for (int i = 0; i < a.length; i++)
    {
        printf("%d ", a.elem[i]);
    }
    printf("\n");
    // a[] = {1,2,3,4,5,6}
    va b;
    b.length = 5;
    b.elem = (int *)malloc(sizeof(int) * a.length);
    for (int i = 0; i < b.length; i++)
    {
        b.elem[i] = 2 * i;
    }
    printf("b= ");
    for (int i = 0; i < b.length; i++)
    {
        printf("%d ", b.elem[i]);
    }
    printf("\n");
    // b[] = {0,2,4,6,8}

    int x;
    for (int i = 0; i < b.length; i++)
    {
        x = b.elem[i];
        if (!table_equal(a, x))
        {
            table_insert(a, x);
            a.length += 1;
        }
    }
    printf("a= ");
    for (int i = 0; i < a.length; i++)
    {
        printf("%d ", a.elem[i]);
    }

    free(a.elem);
    free(b.elem);
    return 0;
}
