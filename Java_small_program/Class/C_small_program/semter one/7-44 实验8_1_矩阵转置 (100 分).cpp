#include <stdio.h>
int main(){
int n,m;
scanf("%d %d",&n,&m);
//int a[n][m];
int b[m][n];
for(int i=0;i<n;i++){
	for(int cnt=0;cnt<m;cnt++){
		scanf("%d",&b[cnt][i]);

	}
} 

for(int i=0;i<m;i++){
	for(int cnt=0;cnt<n-1;cnt++){
		printf("%d ",b[i][cnt]);
	}
	printf("%d\n",b[i][n-1]);
}



return 0;
}

