#include <stdio.h>
int main() {
	int n;
	scanf("%d",&n);
	char a[n][50];
	int b[n];
	for(int i=0; i<n; i++) {
		scanf("%s",&a[i][0]);
	}
	getchar();
	for(int i=0; i<n; i++) {
		scanf("%d",&b[i]);
	}
	for(int cnt=0; cnt<n; cnt++) {
		for(int i=0; i<n; i++) {
			if(b[cnt]==i) {
				printf("%s\n",a[i]);
			}
		}
	}
	return 0;
}

