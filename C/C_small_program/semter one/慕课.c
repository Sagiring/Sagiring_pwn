#include<stdio.h>

int main(){
	int ru,chu,ru2,i;
	
	scanf("%d",&ru);
	
	for(i=0;ru==0;i++)
	{
		ru2=ru%10;
		ru2=ru2+(ru%10)*10*i;
		ru=ru/10;
		printf("%d",ru2);
	}
	
	
	
	
	
	return 0;
}
