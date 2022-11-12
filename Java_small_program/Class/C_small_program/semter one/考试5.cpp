#include <stdio.h>
int main(){
int cnt,a=1,b=1,c,result,n,i;

scanf("%d",&cnt);



for(;cnt>0;cnt--){
	
	scanf("%d",&n);
	a=1;
	b=1;
	if(n<=2){
		result=1%3;
		printf("%d\n",result);
	}else{
	
	
	for(i=3;i<=n;i++){
	
	c=a+b;
	if(a>=b){
	b=c;	
	}else{
	a=c;
	}
	}
	result=c%3;
	printf("%d\n",result);
	}
	
}



return 0;
}

