#include <stdio.h>
int main(){
char a[101];
char b[]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
int c[52]={0},loc=0;
//printf("%c",b[0]);
gets(a);
for(int i=0;a[i]!='\0';i++){
	for(int cnt=0;cnt<52;cnt++){
		if(a[i]==b[cnt]){
			loc=cnt;
			c[loc]++;
		}
	}
	
	
}
for(int i=0;i<52;i++){
	if(c[i]!=0){
		printf("The character %c has presented %d times.\n",b[i],c[i]);
	}
}


return 0;
}

