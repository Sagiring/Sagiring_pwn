#include <stdio.h>
int main() {
	int i,n,key,is=0;
	scanf("%d",&i);
	int a[i];
	for(int cnt=0; cnt<i; cnt++) {
		scanf("%d",&a[cnt]);
	}
	scanf("%d",&n);
	for(int cnt=0; cnt<n; cnt++) {
		scanf("%d",&key);
		for(int x; x<i; x++) {
			if(a[x]==key) {
				if(x!=0&&x!=i-1) {
					printf("%d %d\n",a[x-1],a[x+1]);
					is=1;
				} else if(x==0) {
					printf("%d\n",a[x+1]);
					is=1;
				} else if(x==i-1) {
					printf("%d\n",a[x-1]);
					is=1;
				}
			}
			if(is==1) {
				break;
			}
		}
		if(is==0) {
			printf("NULL\n");
		}
		is=0;
	}
	return 0;
}

