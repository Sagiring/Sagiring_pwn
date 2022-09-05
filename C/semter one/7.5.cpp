#include <stdio.h>
int main() {
	int i,sum=0,cnt,x,line;

	scanf("%d",&line);




	for(cnt=0; cnt<line; cnt++) {
		sum=0;

		for(x=0; x!=-1;) {
			scanf("%d",&x);
			for(i=2; i<=x; i++) {
				if(x%i==0&&i!=x) {
					break;
				} else if(i==x) {
					sum++;
				}

			}
		}
		printf("%d\n",sum);
	}











	return 0;
}

