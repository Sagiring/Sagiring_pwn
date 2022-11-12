#include<stdio.h>

int main(){
	int a1,result;
	scanf("%d",&a1);
	while(a1>0){
		result=result*10+a1%10;
		a1/=10;
	
	}
		printf("%d",result);
	
	
	
	
	
	
	return 0;
}
