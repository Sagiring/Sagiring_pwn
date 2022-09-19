#include <stdio.h>
int main() {
	int ge;
	scanf("%d",&ge);
	int a[ge],b[ge];
	for(int i=0; i<ge; i++) {
		scanf("%d",&a[i]);
	}
	for(int i=0; i<ge; i++) {
		scanf("%d",&b[i]);
	}
	int c;
	for(int i=0; i<ge; i++) {
		c=a[i];
		a[i]=a[b[i]];
		a[b[i]]=c;
	}
	for(int i=0; i<ge-1; i++) {
		printf("%d ",a[i]);
	}
	printf("%d\n",a[ge-1]);

	return 0;
}

