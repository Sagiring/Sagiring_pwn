#include <stdio.h>
int main(){
int a,b,cnt=0,i1;
scanf("%d %d",&a,&b);
for(int i=a;i<=b;i++){
	if(i%7==0){
		cnt++;
	}else{
	
	i1=i;

	for(int n=1;i1!=0;n++){
		if(i1%10==7){
			cnt++;
			break;
		}
		i1/=10;
	}
	
}
	
}
printf("%d",cnt);




return 0;
}

