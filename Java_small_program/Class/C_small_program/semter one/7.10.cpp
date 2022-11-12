#include <stdio.h>
#include <math.h>
int main(){
	
double a,b,c,s,p;
scanf("%lf %lf %lf",&a,&b,&c);
if(a+b>c&&a+c>b&&b+c>a){

p=(a+b+c)/2;
s=sqrt(p*(p-a)*(p-b)*(p-c));
printf("%.3f",s);

}else{
	printf("The edges cannot make up of a triangle.");
}



return 0;
}

