//���������� ���������£�
#include<stdio.h>

int getDigit(long long n); 

int main()
{
    long long     n ;
    int            len ;

    scanf("%lld",&n);
    len = getDigit(n) ;
    if (len > 1)
        printf("The integer %lld has %d digits.\n",n, len) ;
    else
        printf("The integer %lld has %d digit.\n",n, 1) ;
    return 0 ;    
}

/* ����������д�� */
int getDigit(long long n){
	int cnt=0;
	
	for(cnt=0;n!=0;cnt++){
		n/=10;
	}
	
return cnt;
}
