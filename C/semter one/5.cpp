#include <stdio.h>
int main(){
	int a,b,c;
scanf("%d %d",&a,&b);
if(a>b){
	printf("The larger number is %d, the smaller number is %d.",a,b);
}else if(a<b){
	printf("The larger number is %d, the smaller number is %d.",b,a);
}else{
	printf("The two numbers are equal.");
}




return 0;
}

