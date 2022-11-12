#include <stdio.h>
#include <math.h>

void win(int a,int b) {
	if(b>22||a>22) {
		printf("error");
	} else if((a==20)&&(b==21||b==22)) {
		printf("B win");
	} else if(b==20&&(a==21||a==22)) {
		printf("A win");
	} else if(a==b&&a>20) {
		printf("error");
	} else if((a==21&&b==22)||(a==22&&b==21)){
		printf("error");
	}
	
	
	
	else  {
		if(a>b) {
			printf("A win");
		} else if(a<b) {
			printf("B win");
		} else if(a==b) {
			printf("no result");
		}
	}
}

int main() {
//	for(int i=0; i<10; i++) {

		int a,b;
		scanf("%d %d",&a,&b);
		win(a,b);
//		printf("\n");
//	}






	return 0;
}

