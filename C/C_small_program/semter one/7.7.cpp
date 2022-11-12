#include <stdio.h>
int main(){
long n;
int cnt,x,i,sum;

scanf("%ld",&n);

for(i=1;i<=n;i++){
	for(x=i;x!=0;cnt++){
		x/=10;
	}
	sum+=cnt;
	cnt=0;
}
printf("%d",sum);
return 0;
}

