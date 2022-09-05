#include <stdio.h>
int main(){
int n,i,cnt=1;
double result=1,mu=1;


scanf("%d",&n);
if(n==0){
	printf("%.0f",result);
}else{

for(i=n+1;i<=2*n;i++){
	
result=i*result;

cnt=i-n;


result=result/cnt;

}



result=result/cnt+1;

printf("%.0f",result);


}

return 0;
}

