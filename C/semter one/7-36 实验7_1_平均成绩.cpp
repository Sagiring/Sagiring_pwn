#include <stdio.h>
int main() {
	int i,sum=0;
	double result=0;
	scanf("%d",&i);
	int a[i];
	for(int cnt=0; cnt<i; cnt++) {

		scanf("%d",&a[cnt]);
	}
	for(int cnt=0; cnt<i; cnt++) {

		sum+=a[cnt];
	}

	result=1.0*sum/i*1.0;
	printf("%.2f",result);

	return 0;
}

