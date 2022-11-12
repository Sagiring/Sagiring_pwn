#include <stdio.h>
int main(){
int a,cnt=0,x=0,y=0,z=0;
//float result;
do{
	scanf("%d",&a);
	if(a!=0){
		cnt++;
	}
	if(a%3==0&&a%5!=0&&a%7!=0){
		x++;
	}
		if(a%3!=0&&a%5==0&&a%7!=0){
		y++;
	}
		if(a%3!=0&&a%5!=0&&a%7==0){
		z++;
	}
}while(a!=0);

printf("%.2f%%\n",x*100.0/cnt);
printf("%.2f%%\n",y*100.0/cnt);
printf("%.2f%%",z*100.0/cnt);




return 0;
}

