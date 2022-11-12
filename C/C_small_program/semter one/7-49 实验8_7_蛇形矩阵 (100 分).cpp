#include <stdio.h>
int main() {
	int n=0,x=1,line=1,y,is=0;
	scanf("%d",&n);
	int a[n][n];
	a[0][0]=x;
	x++;

	for(int i=0; i<n/2; i++) {
		for(int cnt=line,y=0; cnt>=0; cnt--,y++) {
			a[cnt][y]=x;
//			(1,0)->(0,1)
			x++;
		}
		if((n%2==0)&&(line+1==n)) {
			is=1;
			break;

		}
		line++;
		for(int cnt=0,y=line; y>=0; cnt++,y--) {

			a[cnt][y]=x;
//			n>2 (0,2)->(1,1)->(2,0)
			x++;
		}
		line++;
	}
//testing
	line=1;
	for(int i=0; i<n/2; i++) {

		for(int cnt=n-1,y=line; y<n; cnt--,y++) {
			if(is==1&&line==1) {
				break;
			}
			a[cnt][y]=x;
//			(1,0)->(0,1)
			x++;
		}
//		if((n%2==0)&&(line+1==n)) {
//			break;
//
//		}

		line++;
		if(is==1&&line==2){
			line=1;
		}
		for(int cnt=line,y=n-1; cnt<n; cnt++,y--) {

			a[cnt][y]=x;
//			n>2 (0,2)->(1,1)->(2,0)
			x++;
		}
		line++;
	}
//	testing

	for(int i=0; i<n; i++) {
		for(int cnt=0; cnt<n-1; cnt++) {
			printf("%d ",a[i][cnt]);
		}
		printf("%d\n",a[i][n-1]);
	}



	return 0;
}

