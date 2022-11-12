#include <stdio.h>
int main() {
	char a[101],zuo=0,you=0,is=0;
//	for(int i=0;a[i]!='\n';i++){
//
//	scanf("%c",&a[i]);
//}
	gets(a);
	for(int i=0; a[i]!='\0'; i++) {
		if(a[i]==')'&&is==0){
			break;
		}
			if(a[i]=='(') {
				zuo++;
				is=1;
			}
		if(a[i]==')'&&is==1) {
			you++;
		}
	}



	if(zuo==you&&is==1) {
		printf("parentheses match!");
	} else  {
		printf("parentheses do not match!");
	}

	return 0;
}

