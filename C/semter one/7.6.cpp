#include <stdio.h>
int main() {
	int turenum,i,j,killer=5,ture,noture;
	int a[5][2];
	scanf("%d",&turenum);
	for(i=0; i<5; i++) {
		for(j=0; j<2; j++) {
			scanf("%d",&a[i][j]);
		}
	}
for(killer=5;killer<10;killer++){
	for(i=0;i<5;i++){
		if(a[i][0]==killer){
			if(a[i][1]==1){
				ture++;
			}else{
				noture++;
			}
	}else{
		if(a[i][1]==0){
			ture++;
		}else{
			noture++;
		}
	}
}
if(ture==turenum&&noture==5-turenum){
	printf("%d",killer);
	break;
}	
ture=0;
noture=0;		
}
	return 0;
}

