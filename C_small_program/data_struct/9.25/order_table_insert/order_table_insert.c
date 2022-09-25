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

int main()
{
    va va;
    va.length = 6;
    va.elem = (int *)malloc(sizeof(int) * va.length);
    int x;
    scanf("%d", &x);

    for (int i = 0; i < 6; i++)
    {
        va.elem[i] = i + 1;
    }

    table_insert(va, x);
    va.length += 1;

    printf("a= ");
    for (int i = 0; i < va.length; i++)
    {
        printf("%d ", va.elem[i]);
    }

    free(va.elem);
    return 0;
}
