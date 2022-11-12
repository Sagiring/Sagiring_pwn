#include <stdio.h>
int main() {
	int n,m,gong,yin=1,a,i=1,b;
	scanf("%d %d",&n,&m);
	if(n<m) {
		a=n;
		n=m;
		m=a;
	}
	for(int i=1; i<=m; i++) {
		gong=i*n;
		if(gong%m==0) {

			break;
		}
	}

	b=m;
	a=n;

	while(i!=0) {
		i=a%b;
		a=b;
		if(i==0) {
			yin=b;
		} else {


			b=i;
		}
	}
	yin=b;
	printf("%d %d",yin,gong);



	return 0;
}

