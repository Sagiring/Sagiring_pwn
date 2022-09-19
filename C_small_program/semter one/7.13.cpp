#include <stdio.h>

int main(){
char a[101];
int b=0,c=0,d=0,e=0;
gets(a);
for(int i=0;a[i]!='\0';i++){
	if(a[i]==' '){
		c++;
	}else if((a[i]<='Z'&&a[i]>='A')||(a[i]<='z'&&a[i]>='a')){
		b++;
	}else if(a[i]<='9'&&a[i]>='0'){
		d++;
	}else{
		e++;
	}
}

printf("%d %d %d %d",b,c,d,e);



return 0;
}

