#include <stdio.h>
#include<math.h>
void f(int n,int a){
	if(n/10==0){
		printf("%d",n);
			if(a==0){
			printf(" ");
		}
		
	}else{
		f(n/10,0);
		printf("%d",n%10);
		if(a==0){
			printf(" ");
		}
	}
}
int main() {
	int n,cnt,i=0;
	scanf("%d",&n);
f(n,1);
}

