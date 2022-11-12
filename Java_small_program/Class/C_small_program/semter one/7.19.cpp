#include <stdio.h>
int main(){
char a[101];
gets(a);
for(int i=0;a[i]!='\0';i++){
	if((a[i]>='x'&&a[i]<='z')||(a[i]>='X'&&a[i]<='Z')){
		a[i]-=26;
	}
	a[i]+=3;
	printf("%c",a[i]);
}





return 0;
}

