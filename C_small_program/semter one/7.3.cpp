#include <stdio.h>
int main(){
int money,piece,cnt=0,x,y,z;

scanf("%d %d",&money,&piece);

for(x=0;x<=piece;x++){
	for(y=0;x+y<=piece;y++){
		for(z=0;x+y+z<=piece&&x+2*y+5*z<=money;z++){
			
			if(x+2*y+5*z==money&&x+y+z==piece){
				cnt++;
			}
			
			
			
		}
	}
}

printf("%d",cnt);




return 0;
}

