#include <stdio.h>
int main(){
	int cnt;
	int n,sum=0,max,min;
	scanf("%d",&cnt);
	for(int i=0;i<cnt;i++){
		scanf("%d",&n);
		sum+=n;
		if(i==0){
			max=n;
			min=n;
		}else{
			if(n>max){
				max=n;
			}else if(n<min){
				min=n;
			}
		}
	}



printf("%d %d %d",sum,max,min);


return 0;
}

