#include <stdio.h>
int main(){
float a[6][5]={{0},{0},{0},{0},{0},{0}};
int n,who,which;
float much=0.0,sum=0.0;
scanf("%d",&n);
for(int i=0;i<n;i++){
scanf("%d %d %f",&who,&which,&much);

a[which-1][who-1]+=much;
	
}

for(int i=0;i<4;i++){
	for(int cnt=0;cnt<5;cnt++){
		sum+=a[cnt][i];
	}
	a[5][i]=sum;
	sum=0.0;
}
for(int i=0;i<6;i++){
	for(int cnt=0;cnt<4;cnt++){
		sum+=a[i][cnt];
	}
	a[i][4]=sum;
	sum=0.0;
}



for(int i=0;i<6;i++){
	for(int cnt=0;cnt<5-1;cnt++){
		printf("%.1f\t",a[i][cnt]);
		
	}
	printf("%.1f\n",a[i][4]);
}

return 0;
}

