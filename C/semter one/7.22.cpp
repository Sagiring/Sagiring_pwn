#include <stdio.h>
int main(){
	int n,sum;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		if(i%3==0&&i%7==0){
			sum+=i;
		}
	}
printf("%d",sum*sum);



return 0;
}

