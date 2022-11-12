#include <stdio.h>
int main() {
	int i,a,b,c,result,cnt;

	scanf("%d",&i);

	for(cnt=0; cnt<i; cnt++) {
		scanf("%d %d %d",&a,&b,&c);
		if(a<75||b<75||c<75) {
			result=0;
		} else {
			if(a+b+c>=240) {
				result=1;
			} else {
				result=0;
			}
		}
		if(result==1) {
			printf("Yes\n");
		} else {
			printf("No\n");
		}
	}





	return 0;
}

