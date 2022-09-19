#include <stdio.h>
int main() {

	int l,c,n,i,cnt,sn,k;
	scanf("%d %d %d",&l,&c,&n);


	for(i=0; i<(c*(n+1))+1; i++) {
		printf("*");
	}
	printf("\n");

	for(sn=0; sn<l; sn++) {



		for(cnt=0; cnt<3; cnt++) {
			printf("*");
			
			for(i=0; i<c; i++) {
				
				for(k=0;k<n;k++){
					printf(".");
				}
				
				printf("*");
				
			}
			printf("\n");
		}
				for(i=0; i<(c*(n+1))+1; i++) {
			printf("*");
		}
		printf("\n");

	}


	return 0;
}

