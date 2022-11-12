#include <stdio.h>
#include <math.h>
int main() {
	int a,b;
	scanf("%d %d",&a,&b);

	if(a>23||b>23) {
		printf("error");
	} else {
		if(abs(a-b)<=3) {

			if(a>b) {
				printf("A win");
			} else if(a<b) {
				printf("B win");
			}else{
				printf("error");
		 }
			
		}else{
		
				printf("error");
		}

	}




	return 0;
}

