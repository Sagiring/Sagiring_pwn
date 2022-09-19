#include<stdio.h>

int countBinary(int);

int main()
{
    int        n;

    scanf("%d",&n);
    printf("%d\n",countBinary(n));

    return 0 ;
}

/* 请在这里填写答案 */
int countBinary(int n){
	int i=0;
	

	if(n/2==0){
		
	return i+=1;
	}else{
		
	i=countBinary(n/2);

	return i+=1;
	
	}
	

}
