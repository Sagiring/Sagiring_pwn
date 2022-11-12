#include <stdio.h>

int main(){
	int time1;
	int past;
	int hour,minute;
	scanf("%d %d",&time1,&past);
	minute=time1%100;
	hour=time1/100;
	
	hour+=past/60;
	minute+=past%60;
	
	if(minute>=60){
      minute-=60;
	  hour+=1;				
	}
	if(minute<0){
		minute+=60;
		hour-=1;
	}
	if(minute==0){
	printf("%d00",hour,minute);
	}	
	else{
	printf("%d%d",hour,minute);
}
	
	return 0;
}
