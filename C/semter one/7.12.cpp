#include <stdio.h>

int main() {
	int x,y,sum=1;
	scanf("%d %d",&x,&y);
	if(y==0) {
		sum=1;
	} else {

		for(; y>0; y--) {
			sum*=x;
		}
	}
	printf("%d",sum);



	return 0;
}

