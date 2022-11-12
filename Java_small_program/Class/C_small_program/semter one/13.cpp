#include<stdio.h>

int main(){

float open,close,high,low;
	
scanf("%f %f %f %f",&open,&high,&low,&close);

if(close<open){
	printf("BW-Solid");
}else if(close>open){
	printf("R-Hollow");
}else if(close==open){
	printf("R-Cross");
}
int a=0;

if(low<open&&low<close){
	printf(" with Lower Shadow");
	a=1;
}else if (high>open&&high>close&&a==0){
	printf(" with Upper Shadow");
}
if (high>open&&high>close&&a==1){
	printf(" and Upper Shadow");
}
	
	
	
	
	
	
	
	return 0;
}
