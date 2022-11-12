#include <stdio.h>
int main() {
	int m,n,a1,a2,sum=0,is=0;
	scanf("%d %d",&m,&n);
	int a[m][n];
	for(int i=0; i<m; i++) {
		for(int cnt=0; cnt<n; cnt++) {
			scanf("%d",&a[i][cnt]);
		}
	}
	scanf("%d %d",&a1,&a2);

	
	if(a1==1||a2==1||a1==m||a2==n) {
		
		if(a1==1&&a2==1) {
			sum+=a[1][1];
			sum+=a[1][0];
			sum+=a[0][1];
		} else if(a1==1&&a2==n) {
			sum+=a[0][n-2];
			sum+=a[1][n-1];
			sum+=a[1][n-2];
		} else if(a1==m&&a2==1) {
			sum+=a[m-1][1];
			sum+=a[m-2][0];
			sum+=a[m-2][1];
		} else if(a1==m&&a2==n) {
			sum+=a[m-2][n-2];
			sum+=a[m-1][n-2];
			sum+=a[m-2][n-1];
		} else {
			
			
			if(a1==1) {
				sum+=a[0][a2-2];
				sum+=a[0][a2];
				for(int i=0; i<3; i++) {
					sum+=a[1][a2-2+i];
				}
			} else if(a2==1) {
				sum+=a[a1-2][0];
				sum+=a[a1][0];
				for(int i=0; i<3; i++) {
					sum+=a[a1-2+i][1];
				}
			} else if(a1==m) {
				sum+=a[m-1][a2-2];
				sum+=a[m-1][a2];
				for(int i=0; i<3; i++) {
					sum+=a[m-2][a2-2+i];
				}
			} else if(a2==n) {
				sum+=a[a1-2][n-1];
				sum+=a[a1][n-1];
				for(int i=0; i<3; i++) {
					sum+=a[a1-2+i][n-2];
				}
				}}
			
		
}else{


		for(int i=a1-2; i<a1+3-2; i++) {
			for(int cnt=a2-2; cnt<a2+3-2; cnt++) {
				sum+=a[i][cnt];

			}
		}
		sum-=a[a1-1][a2-1];
	
}

	printf("%d",sum);
	return 0;
}


