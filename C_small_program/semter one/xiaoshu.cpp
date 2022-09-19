#include<stdio.h>

int main(){
	int high,pa,hua,minute=0;
	high-=1;
	
	scanf("%d %d %d",&high,&pa,&hua);
	high-=1;
	
	if(high<=0){printf("%d",minute);
	}else{
	
	
	while(high>0){
		
		high-=pa;
		minute++;
		
		if(high<0){
		printf("%d",minute);
		}else{
		
		high+=hua;
		minute++;}
		
		
		
		
		
	}
}

	
	
	return 0;
}
