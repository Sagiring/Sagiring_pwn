#include <stdio.h>
#include <math.h>
int main(){
int x,i,cnt,sum=0,wei=1;
scanf("%d",&x);
if(x<=10000&&x>=1){
if(x==1){
	goto out;
}
 for(i=x*x;i>=10;i/=10){
 	sum=sum*10+i%10;
 }
//printf("%d\n",sum);
cnt=sum;
for(sum=0;cnt>0;cnt/=10){
		sum=sum*10+cnt%10;
	wei++;
}

while(sum!=0){
	sum=sum%(int)pow(10,wei);
	wei--;
	if(sum==x){
		break;
	}
}


//printf("%d",wei);

if(sum==x){
out:	printf("Yes");
}else{
	printf("No");
}
}else{
	printf("%d out of range",x);
}

return 0;
}

