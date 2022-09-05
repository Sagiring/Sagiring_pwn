#include<stdio.h>
#include<math.h>
int main(){
	float a,b,c,derta,x1,x2,xu1,xu2,shi;
	
	scanf("%f %f %f",&a,&b,&c);
	
if(abs(a-0)<1e-6){
	printf("The equation is not quadratic.");
}else{
derta=b*b-4*a*c;
x1=(-b+sqrt(derta))/(2*a);
x2=(-b-sqrt(derta))/(2*a);

if(derta<0){
	
	derta=-derta;
    xu1=sqrt(derta)/(2*a);
    xu2=-sqrt(derta)/(2*a);
    shi=(-b)/(2*a);
   
    printf("The equation has two complex roots: %.4f+%.4fi and %.4f%.4fi.",shi,xu1,shi,xu2);
	
}else if(abs(derta)<1e-6){
	printf("The equation has two equal roots: %.4f",x1);}
	else if(derta>0){
printf("The equation has two distinct real roots: %.4f and %.4f.");
	}
}	

	
	
	
	
	
	
	
	
	return 0;
}
