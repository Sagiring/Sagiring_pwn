#include <stdio.h>
#include <stdlib.h>

typedef int SElemType;

typedef struct
{
    SElemType *base[2];
    SElemType *top[2];
    int length;
} tws;

int STACK_ININT_SIZE = 10;

int InitStack(tws *t)
{
    t->base[0] = (SElemType *)malloc(STACK_ININT_SIZE * sizeof(SElemType));
    if (!t->base[0])
    {
        exit(-1);
    }
    t->top[0] = t->base[0];
    t->base[1] = &(t->base[0][STACK_ININT_SIZE - 1]);
    t->top[1] = t->base[1];
    t->length = STACK_ININT_SIZE;
    return 0;
}

int Push(tws *t, int i, SElemType x)
{   
    if (t->top[0] == t->top[1])
    {
        return -1;
        // 空间分配已满
    }
    *t->top[i]++= x;
    return 0;
}

int Pop(tws *t, int i, SElemType *x)
{
  
    if (t->top[i] == t->base[i])
    {
        return -1;
        // 空间分配已满
    }
    *x = *--t->top[i];
    
    return 0;
}

int main(int argc, char const *argv[])
{
    tws* t;
    int i = 0;
    int x = 10;
    SElemType result ;
    InitStack(t);
    Push(t,i,x);
    Pop(t,i,&result);
    printf("%d",result);

    return 0;
}
