#include <stdio.h>
int main() {
	int c,l,sum=0;
	scanf("%d %d",&c,&l);
	int a[c+2][l+2];
	int n,x,y;
	scanf("%d",&n);
	for(int i=0; i<c+1; i++) {
		for(int cnt=0; cnt<l+2; cnt++) {
			a[i][cnt]=0;
			
		}
	}
	for(int i=0; i<c+2; i++) {
		a[i][0]=-100;
		a[i][l+1]=-100;
	}
	for(int cnt=0; cnt<l+2; cnt++) {
		a[0][cnt]=-100;
		a[c+1][cnt]=-100;
	}

	for(int j=0; j<n; j++) {
		scanf("%d %d",&x,&y);
		a[x][y]+=1;
		a[x+1][y]+=1;
		a[x-1][y]+=1;
		a[x][y+1]+=1;
		a[x][y-1]+=1;
		a[x+1][y+1]+=1;
		a[x-1][y-1]+=1;
		a[x+1][y-1]+=1;
		a[x-1][y+1]+=1;

	}

	for(int i=1; i<c+1; i++) {
		for(int cnt=1; cnt<l+1; cnt++) {
			if(a[i][cnt]>0) {
				sum++;
			}
		}
	}
	printf("%d",sum);




	return 0;
}

