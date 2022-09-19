#include <stdio.h>
int main(){
int n,year;

	int sky,gro;
	char a[]={'0','A','B','C','D','E','F','G','H','I','J','K','L','\0'};
scanf("%d",&n);
for(int x=0;x<n;x++){
	scanf("%d",&year);

	year=(year-4)%60;
	sky=year%10;
	gro=year%12;

	printf("%d",sky);
	printf("%c\n",a[gro+1]);
	
	
} 





return 0;
}

