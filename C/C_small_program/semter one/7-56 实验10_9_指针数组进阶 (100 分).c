#include <stdio.h>
#include <string.h>
void swap(char** a,char** b);


int main() {
	int n=0,loc=0,i=0,is=0;
	scanf("%d",&n);
	char *p[n];
	char str[100];

	getchar();

	for(int cnt=1; cnt<=n; cnt++) {
		gets(&str[i]);
		if(cnt==1) {
			p[0]=&str[0];
		}

		while(str[i]!='\0') {
			i++;
		}

		if(str[i]=='\0') {
			i++;
//			loc=i;
		}


		p[cnt]=&str[i];

//		getchar();
	}
	for(int cnt=1; cnt<n; cnt++) {
		for(i=0; i<n-cnt; i++) {
			is=strcmp(p[i],p[i+1]);
			//输入两个字符串地址
			//前>后 则返回>0 
			if(is>0) {
				//升序 ->从小到大 
				swap(&p[i],&p[i+1]);
			}
		}
	}
	for(int cnt=0; cnt<n; cnt++) {
		printf("%s\n",p[cnt]);
	}


	return 0;
}
void swap(char** a,char** b) {
	char* p;
	p=*b;
	*b=*a;
	*a=p;
}
