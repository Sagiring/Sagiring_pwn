#include <stdio.h> 
int main(){
	int a,b,cnt=1,sum=0,i;
	scanf("%d %d",&a,&b);


while(a<=b){
	
//	if(cnt<=5){
//		printf(" ");
//	}
	
	printf("%5d",a);
	
	
	
	
   while(cnt==5&&a!=b){
   	printf("\n");
   	cnt=0;
   }
    sum+=a;

    a++;
    cnt++;
   }
//   printf(" ");
//   printf("%d",a);
//   sum+=a;
   printf("\n");
   printf("Sum = %d",sum);

	
	return 0;
}
