#include<stdio.h>

int main(){

double height;
int weight;
double result;

scanf("%d %lf",&weight,&height);
result=weight/(height*height);
	
	
	if(result<18.5){
		printf("Underweight");
	}else if(result>=18.5&&result<24){
		printf("Normal");
	}else if(result>=24){
		printf("%.6lf\n",result);
		printf("Overweight");
		}
		
	
	return 0;
}

	
	
	
	
	
	
	
	

