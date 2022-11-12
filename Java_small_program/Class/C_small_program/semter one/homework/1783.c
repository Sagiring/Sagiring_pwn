#include <stdio.h>
//1783

int main()
{
	double a;
	double b;
	double c;
	double d;
	double result=0;
	
	scanf("%lf %lf %lf %lf",&a,&b,&c,&d);
	result=(a+b)*(a-b)+c/d;
	
	printf("%f",result);
	
	
	
	
	
	
	return 0;
}
