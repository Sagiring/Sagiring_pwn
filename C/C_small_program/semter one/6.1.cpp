#include <stdio.h>

void reverse(int n) ;

int main() {
	int     n;

	scanf("%d",&n);
	reverse(n) ;
	printf("\n");
	return 0;
}

/* 请在这里填写答案 */
void reverse(int n) {
	printf("%d",n%10);
	if(n<10) {
	
	} else {
		if(n>1) {
			reverse(n/10);
		}

	}
}
