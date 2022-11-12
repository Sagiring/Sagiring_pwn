#include <stdio.h>
#define maxsize 10
typedef struct
{
    int j;
    int e;
} Triple;

typedef struct
{
    Triple data[maxsize];
    int mu, nu;
    int row[maxsize];
} DSMatrix;

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}

int find_Matrix_elem(DSMatrix A, int iloc, int jloc)
{
    int many_row_num;
    int pre_row_num;
    for (int i = 0; i < maxsize; i++)
    {

        pre_row_num = A.row[i];
        many_row_num = A.row[i + 1] - A.row[i];

        for (int row_num = 0; row_num < many_row_num; row_num++)
        {
            if (i != iloc)
            {
                break;
            }
            else
            {
                if (A.data[pre_row_num + row_num].j == jloc)
                {
                    return A.data[pre_row_num + row_num-1].e;
                }
            }
        }
    }

    return -1;
}