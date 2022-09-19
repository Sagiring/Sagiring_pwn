#include <stdio.h>
#include <math.h>

int main() {
	int a,b;
	scanf("%d %d",&a,&b);
	if(a<=21&&b<=21) {
		if(a==b) {
			printf("error");
		} else if(a>b) {
			printf("A win");
		} else {
			printf("B win");
		}

	} else {


		if(abs(a-b)==1||a==b) {
			printf("error");
		} else {
			if(a>b) {
				printf("A win");
			} else {
				printf("B win");
			}
		}


	}



	return 0;
}

