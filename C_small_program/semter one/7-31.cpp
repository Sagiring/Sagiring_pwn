#include <stdio.h>
int main(){
int n;
scanf("%d",&n);
for(int i=n;;i++){
	if(i%5==1&&i%6==5&&i%7==6&&i%11==10){
		printf("%d",i);
		break;
	}
}




return 0;
}

