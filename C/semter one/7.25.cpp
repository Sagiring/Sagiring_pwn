#include <stdio.h>
int main(){
int n,cnt=0,result=0,ren,recnt=0;
scanf("%d",&n);
for(ren=n;ren>0;cnt++){
	ren/=10;
}
//printf("%d\n",cnt);

for(int i=0;i<cnt;i++){
	result=result*10+n%10;
	n/=10;
}
for(ren=result;ren>0;recnt++){
	ren/=10;
}
if(recnt==cnt){

printf("%d",result);

}else if(recnt!=cnt){
	printf("The number cannot be changed.");
}
return 0;
}

