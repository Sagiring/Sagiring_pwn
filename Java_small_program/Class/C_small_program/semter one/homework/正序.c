#include <stdio.h>

int main(){
	int ru;
	scanf("%d",&ru); 
   // int cnt=-1;
	int t1=ru;
	int chu;
	int t=1;
	while(ru>9){

	    
		t*=10;
		//printf("%d\n",t);
		ru=ru/10;
	}
	printf("t=%d\n",t);
	int x=ru;
	int q=t;
	while(t1>0){
		x=x*10+(t1/q);
		t1=t1%q;
		q/=10;
	printf("t1=%d\n",t1);
	}
	  printf("t1=%d\n",t1); 
	
 	while(x>0){
 	chu=x/t;
 	x=x%t;
	printf("%d",chu);
	if(x>0){
		printf(" ");
	}
	t/=10;	
	 }
	
	
	
	
	
	
	
	
	return 0;
}
