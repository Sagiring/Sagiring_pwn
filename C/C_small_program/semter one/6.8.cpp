#include<stdio.h>

int    fuc(int n) ;

int main()
{
    int n ;

    scanf("%d",&n); 
    printf("%d\n",fuc(n));

    return 0 ;
}

/* ����������д�� */
int    fuc(int n) {
	int fn;
	if(n==0){
		fn=0;
	}
	if(n>0){
		fn=fuc(n-1)+n*n*n;
	}
	
	
	return fn;
	
	
	
}
