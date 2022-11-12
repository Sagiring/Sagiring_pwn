#include <stdio.h>
#include <math.h>
int main(){
int n,n1,sum=0;
	int i=0;
scanf("%d",&n);
for(n1=n;n1!=0;n1/=10){

sum=sum+(n1%10)*pow(2,i);
i++;
}

printf("%d",sum);




return 0;
}

