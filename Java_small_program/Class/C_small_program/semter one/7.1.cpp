#include <stdio.h>
int main(){

int start=0,i,sum=0;
float result;
 
 for(i=0;i<7;i++){
 	scanf("%d",&start);
 	sum+=start;
 }
result=sum/7.0;
if(result>90){
	printf("A:%.1f",result);
}else if(result<=90&&result>70){
	printf("B:%.1f",result);
}else if(result<=70&&result>50){
	printf("C:%.1f",result);
}else {
	printf("D:%.1f",result);
}



return 0;
}

