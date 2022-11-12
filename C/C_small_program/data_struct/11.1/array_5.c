#include <stdio.h>
#define maxsize 10
typedef struct 
{
    int i,j;
    int e;
}Triple;

typedef struct 
{
    Triple data[maxsize];
    int mu,nu,tu;
}DSMatrix;

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
 
TSMatrix And_Matrix(TSMatrix A,TSMatrix B){
TSMatrix C;
for (int i = 0; i < maxsize; i++)
{
    int iloc = A.data[i].i;
    int jloc = A.data[i].j;
    int result = A.data[i].e;
    for (int cnt = 0; cnt < maxsize; cnt++)
    {
        if(B.data[cnt].i==iloc && B.data[cnt].j==jloc){
            result += B.data[cnt].e;
        }
    }
    C.data[i].i = iloc;
    C.data[i].j = jloc;
    C.data[i].e = result;
}
return C;
 }