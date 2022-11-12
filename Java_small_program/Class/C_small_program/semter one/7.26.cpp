#include <stdio.h>
#include <math.h>
int main(){
	int n,m,x,i,sum=0,cnt;
	scanf("%d %d",&n,&m);
	for(i=1;i<=n;i++){

		 for(cnt=i;cnt!=0;cnt/=10){
		 	
		 	sum=sum+(cnt%10)*(cnt%10);
		 }

		if(i/m==sum){
			printf("%d\n",i);
		}
	sum=0;

}




return 0;
}

