//�����������������£�
#include<stdio.h>

int reverseNum(int) ; 

int main()
{
    int        num ;

    scanf("%d",&num);
    printf("The reverse form of number %d is %d.\n",num,reverseNum(num)) ;

    return 0;
}

/* ����������д�� */
int reverseNum(int x) {
	int result,y;
	
	for(result=0;x!=0;){
	
	y=x%10;
	result=result*10+y;
	x/=10;
		
		
	}
	
	
	
	
	
	
	
	
	
	
	return result;
	
}
