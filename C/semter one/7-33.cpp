#include <stdio.h>
int main(){
int n,k=0,n1;
scanf("%d",&n);
for(n1=n;n1!=0;n1/=10){
	k=k*10+n1%10;
}

if(n==k){
	printf("Yes");
}else{
	printf("No");
}



return 0;
}

