#include <stdio.h>
int main(){
int line,cnt,goods,sum=0;
scanf("%d",&line);
for(int i=0;i<line;i++){
	scanf("%d",&cnt);
	for(int n=0;n<cnt;n++){
		scanf("%d",&goods);
		sum+=goods;
	}	
	if(sum>=100&&sum<200){
	sum-=30;
}else if(sum>=200&&sum<300){
	sum-=70;
}else if(sum>=300&&sum<400){
	sum-=110;
}else if(sum>=400){
	sum-=160;
}
printf("%d\n",sum);
sum=0;
}

return 0;
}

