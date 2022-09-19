#include <stdio.h>
int main() {
	int m,n,max,min,x1,y1,x2,y2,find=0;
	scanf("%d %d",&n,&m);
	int a[n][m];
	for(int i=0; i<n; i++) {
		for(int cnt=0; cnt<m; cnt++) {
			scanf("%d",&a[i][cnt]);
		}
	}
	if(n==1||m==1) {
		if(n==1) {
			max=a[0][0];
			x1=0;
			y1=0;
			for(int i=0; i<m; i++) {
				if(max<a[0][i]) {
					max=a[0][i];
					x1=0;
					y1=i;
				}
			}
		} else {
			min=a[0][0];
			x1=0;
			y1=0;
			for(int i=0; i<n; i++) {
				if(min>a[i][0]) {
					min=a[i][0];
					x1=i;
					y1=0;
				}
			}

		}
		find=1;
	} else {

		for(int i=0; i<n; i++) {
			max=a[i][0];
			x1=i;
			y1=0;
			for(int cnt=0; cnt<m; cnt++) {
				if(max<a[i][cnt]) {
					max=a[i][cnt];
					x1=i;
					y1=cnt;
				}
			}

			min=a[0][y1];
			x2=0;
			y2=y1;
			for(int ai=0; ai<n; ai++) {
				if(min>a[ai][y1]) {
					min=a[ai][y1];
					x2=ai;
					y2=y1;
				}
			}
			if(x1==x2&&y1==y2) {
				find=1;
				break;
			}


		}
	}
	if(find==1) {
		printf("The saddle point is (%d,%d)=%d.",x1,y1,a[x1][y1]);
	} else {
		printf("There is no saddle point in the matrix.");
	}



	return 0;

}
