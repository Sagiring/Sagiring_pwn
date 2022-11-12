#include <stdio.h>
int main(){
int c,l,i,cnt;
scanf("%d %d",&l,&c);

printf("|");
for(i=0;i<c;i++){
	printf("*****|");
}
printf("\n");
//Í·²¿¡ü
 
for(i=0;i<l;i++){
	
	
	printf("|");
	for(cnt=0;cnt<c*2;cnt++){
		printf("  |");
	}
	printf("\n");
	
		printf("|");
	for(cnt=0;cnt<c;cnt++){
		printf("--+--");
		printf("|");
	}
	printf("\n");
	
		printf("|");
	for(cnt=0;cnt<c*2;cnt++){
		printf("  |");
	}
	printf("\n");
	
	printf("|");
for(cnt=0;cnt<c;cnt++){
	printf("*****|");
}
printf("\n");
	
}
return 0;
}

