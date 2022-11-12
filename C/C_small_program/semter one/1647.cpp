#include <stdio.h>
#include <math.h>
int main(){
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	if(a+b>c&&a+c>b&&b+c>a){
	

	double s=0,p=0;
	
	p=(a+b+c)/2;
	s=sqrt(p*(p-a)*(p-b)*(p-c));
	printf("%.3f",s);
	
}else{
	printf("The edges cannot make up of a triangle.");
}
	
	
	
	
	
	return 0;
}
