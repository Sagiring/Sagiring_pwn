#include <stdio.h>
int main(){
double a,b,c,d,result;

scanf("%lf %lf %lf %lf",&a,&b,&c,&d);

if((b*c-d)!=0){

result=a/(b*c-d);
printf("%.1f",result);
}else{
	
	printf("error");
	
}




return 0;
}

