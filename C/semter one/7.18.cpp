#include <stdio.h>
#include <math.h>
int main(){
float a0,a1,a2,a3;
double a,b,fx,fa,fb,x,c,fc;
scanf("%f %f %f %f",&a3,&a2,&a1,&a0);
scanf("%lf %lf",&a,&b);

x=a;
fx=a3*x*x*x+a2*x*x+a1*x+a0;
fa=fx;

x=b;
fx=a3*x*x*x+a2*x*x+a1*x+a0;
fb=fx;
if(fa>0){
	c=a;
	a=b;
	b=c;
	fc=fa;
	fa=fb;
	fb=fc;
}
	x=(a+b)/2;
	fx=a3*x*x*x+a2*x*x+a1*x+a0;


while(fabs(a-b)>10e-4&&fabs(fx)>10e-6){
	x=(a+b)/2;
	fx=a3*x*x*x+a2*x*x+a1*x+a0;
	if(fx<0){
		a=x;
	}else if(fx>0){
		b=x;
	}else if(fx==0){
		x=x;
	}

}


printf("%.2f",x);



return 0;
}

