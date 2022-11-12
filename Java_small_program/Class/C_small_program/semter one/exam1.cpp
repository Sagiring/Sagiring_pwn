#include <stdio.h>
int main(){
	
	char c;
	while(c!='\n'){
			c=getchar()	;
	if(c!='\0') {

			if('A'<=c&&c<='Z') {
				c+='z'-'Z';
			} else if('a'<=c&&c<='z') {
				c-=32;
			}


		}


	printf("%c",c);
}


return 0;
}

