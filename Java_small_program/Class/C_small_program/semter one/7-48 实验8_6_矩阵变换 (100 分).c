#include <stdio.h>
int main() {
	int n,sum=0,min,loc;
	scanf("%d",&n);
	int a[n][n];
	int b[n];
	for(int i=0; i<n; i++) {
		sum=0;
		for(int cnt=0; cnt<n; cnt++) {
			scanf("%d",&a[i][cnt]);
			sum+=a[i][cnt];
		}
		b[i]=sum;
	}
	min=b[0];
	loc=0;

	for(int cnt=0; cnt<n; cnt++) {
		if(b[0]!=-177) {
			min=b[0];
			loc=0;
		}
		for(int x=1; b[x-1]==-177; x++) {

			min=b[x];
			loc=x;
		}
		for(int i=0; i<n; i++) {
			if(b[i]<min&&b[i]!=-177) {
				min=b[i];
				loc=i;
			}
		}

		for(int i=0; i<n-1; i++) {
			printf("%d ",a[loc][i]);
		}
		printf("%d\n",a[loc][n-1]);
		b[loc]=-177;
	}


	return 0;
}

