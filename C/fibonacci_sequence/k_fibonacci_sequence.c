#include <stdio.h>

int k_fibonacci_sequence(int k, int m)
{
    int cnt = 1;
    int result = 1;
    int k_array[k];
    for (int i = 0; i < k; i++)
    {
        k_array[i] = 0;
    }

    k_array[0] = 1;
    while (1)
    {

        if (m == cnt)
        {
            return result;
        }
        else
        {
            if (cnt == 1)
            {
                k_array[1] = result;
            }
            else if (cnt < k)
            {
                result = 0;
                for (int i = 0; i < cnt; i++)
                {
                    result += k_array[i];
                }
                k_array[cnt] = result;
            }
            else
            {
                result = 0;
                for (int i = 0; i < k; i++)
                {
                    result += k_array[i];
                }
                for (int i = 0; i < k - 1; i++)
                {
                    k_array[i] = k_array[i + 1];
                }
                k_array[k - 1] = result;
            }
            cnt++;
        }
    }
}
int main()
{
    int k = 25;
    int m = 26;
    int result = k_fibonacci_sequence(k, m);
    printf("result = %d", result);
    return 0;
}