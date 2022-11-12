#include <stdio.h>
int main() {
	int n,cnt,i;
	scanf("%d",&n);

	for(i=1; i<n+1; i++) {
		for(cnt=n-i; cnt>0; cnt--) {
			printf(" ");
		}
		for(cnt=0; cnt<2*i-1; cnt++) {
			printf("*");
		}

	
			printf("\n");
		
	}
	for(i=n-1; i>0; i--) {
		for(cnt=0; cnt<n-i; cnt++) {
			printf(" ");
		}
		for(cnt=0; cnt<2*i-1; cnt++) {
			printf("*");
		}
		if(i!=1) {
			printf("\n");
		}
	}



	return 0;
}

