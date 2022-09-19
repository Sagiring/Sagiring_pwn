#include <stdio.h>
int main(){

int i,max=0,min=0,cnt,start=0,endif;
scanf("%d",&cnt);

for(;cnt>0;cnt--){
	i=0;
	while(i!=-1){
		scanf("%d",&i);
		if(start==0){
			min=i;
			max=i;
			start++;
		}else if(min>i&&i!=-1){
			min=i;
			}else if(max<i){
				max=i;
			}
		
	}
	endif=(max-min)%3;
	if(endif==0){
		
		printf("%d %d\n",max,min);
	}
	
	
}




return 0;
}

