#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void swap(char** a,char** b);
int main() {
	int n,len,is;
	scanf("%d",&n);
	getchar();
	char tem[1000];
	char **p;
	p=malloc(sizeof(char*)*n);
	for(int i=0; i<n; i++) {
		gets(tem);
		len=strlen(tem);
		p[i]=malloc(sizeof(char)*(len+1));
		strcpy(p[i],tem);
	}
	for(int i=1; i<n; i++) {
		for(int cnt=0; cnt<n-i; cnt++) {
			is=strcmp(p[cnt],p[cnt+1]);
			if(is>0) {
				swap(&p[cnt],&p[cnt+1]);
			}
		}
	}
	for(int i=0; i<n; i++) {
		printf("%s\n",p[i]);

	}
	for(int i=0; i<n; i++) {
		free(p[i]);
	}

	free(p);
	return 0;
}
void swap(char** a,char** b) {
	char *p;
	p=*a;
	*a=*b;
	*b=p;
}
