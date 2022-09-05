#include <stdio.h>

int fact(int n){
	if(n==1){
		return n;
	}
		return n*fact(n-1) ;
//		´Óµ×²¿·µ»Ø 
	
	
	
	
} 

int main(){
	int n;
	
	n=fact(2);
	
	printf("%d",n);






return 0;
}

