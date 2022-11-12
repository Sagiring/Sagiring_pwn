#include <stdio.h>
#include<math.h>
int main(){
	int a,b,result;
	scanf("%d %d",&a,&b);
	
//	1:A win 2:B win 3:no result 4:error
	
	
	
	if(abs(a-b)!=1){
		if(a<11&&b<11){
				result=3;
			}	
//		大比分 
		if(a==11||b==11){
			
		if(a>b){
			result=1;
		}else{
			result=2;
		}
	}
//		不差一分的情况 
		if(a>11||b>11){
//			差一分且加时 
			if(abs(a-b)==2){
//				加时赢 
			   if(a>b){
			   	result=1;
			   }else{
			   	result=2;
			   }
			   
			}else{
			result=0;	
			}
			
		}
//		差一分 
	}else{ if(a<11&&b<11){
		result=3;
//		差一分未结束 
	}else if(a==11||b==11){
		if(abs(a-b)==1){
			result=3;
		} else{
		
		if(a>b){
			result=1;
		}else{
			result=2;
		}}
//		差一分结束 
	}else if(a>11&&b>11){if(abs(a-b)==1){
		result=3;
	}else{
		result=0;
	}	
	}
	}
	if((a>11||b>11)&&abs(a-b)>=3){
		
		result=0;
	}
	
if(a==b){
	result=3;
}
switch (result){
	case 0:
	printf("error");
	break;
	case 1:
	printf("A win");
	break;
	case 2:
	printf("B win");
	break;
	case 3:
	printf("no result");
	break;
		
}
	return 0;
}
