#include <stdio.h>

int findMax(int n) ;

int main() {
	int n ;

	scanf("%d", &n);
	printf("%d\n" , findMax( n ) ) ;

	return 0;
}

/* 请在这里填写答案 */
int findMax(int n) {
	int x,max,i;
	scanf("%d",&x);

	if(n!=1&&x>(i=findMax(n-1))) {
		max=x;
		return max;
	} else {
		if(n==1) {
			return x;
		} else {

			return i;
		}
	}


	return max;
}
