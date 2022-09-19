#include <stdio.h>
#include <string.h>
 #include <stdlib.h>
struct student {
	char name[21];
	int sum;
};
void swap(struct student** a,struct student** b);
int main() {
	int n,is;
	scanf("%d",&n);
	struct student a[n];
	for(int i=0; i<n; i++) {
		scanf("%s",a[i].name);
		scanf("%d",&a[i].sum);
	}
	struct student* p[n];
	for(int i=0; i<n; i++) {
		p[i]=&a[i];
	}
	for(int cnt=1; cnt<n; cnt++) {
		for(int x=0; x<n-cnt; x++) {
			if((p[x]->sum)<(p[x+1]->sum)) {
				swap(&p[x],&p[x+1]);
			}else if(p[x]->sum==p[x+1]->sum){
				is=strcmp(p[x]->name,p[x+1]->name);
				if(is>0){
				swap(&p[x],&p[x+1]);
				}
			}
		}
	}
for(int i=0;i<n;i++){
	printf("Name:%s\n",p[i]->name);
	printf("total:%d\n\n",p[i]->sum);
}

	return 0;
}

void swap(struct student** a,struct student** b) {
	struct student *p;
	p=*a;
	*a=*b;
	*b=p;
}
