#include <stdio.h>
int main() {
	int line,cnt=0,shu,sum=0,isPrime=1;

	scanf("%d",&line);
	for(int i=0; i<line; i++) {

		do {
			scanf("%d",&shu);
			isPrime=1;
			for(cnt=2; cnt<shu/2+1&&shu!=-1; cnt++) {
				if(shu%cnt==0) {
					isPrime=0;
					break;
				}
			}
			if(isPrime&&shu!=-1) {
				sum++;
			}
		} while(shu!=-1);

		printf("%d\n",sum);
		sum=0;



	}







	return 0;
}

