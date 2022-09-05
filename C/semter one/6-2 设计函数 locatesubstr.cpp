//函数被调用进行测试的例子如下：
#include <stdio.h>
#include <string.h>

char *locatesubstr(char *str1,char *str2);
int main() {
	char str1[100],str2[100];
	char *p;
	gets(str1);
	gets(str2);
	p=locatesubstr(str1,str2);

	if(p==NULL)    printf("NULL!\n");
	else    puts(p);

	return 0;
}

/* 请在这里填写答案 */
//函数接口如下：
char *locatesubstr(char *str1,char *str2) {
	char* p=NULL;
	int cnt,is=1;
	for(int i=0; str1[i]!='\0'; i++) {

		if(str1[i]==str2[0]) {
			for(cnt=0; (str2[cnt]!='\0')&&(str1[i+cnt]!='\0'); cnt++) {
				if(str1[i+cnt]!=str2[cnt]||((str1[i+cnt+1]=='\0')&&(str2[cnt+1]!='\0'))){
					is=0;
					break;
				}
			}
			if(is==1) {
				p=&str1[i];
				break;
			}

		}
		is=1;
	}
	return p;
}

