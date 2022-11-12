#include <stdio.h>
int main(){
float dad,mom,height;
int sex;

scanf("%f %f %d",&dad,&mom,&sex);
if(sex==0){
	height=(dad * 0.923 + mom)/ 2.0;
}else{
	height=(dad + mom) * 1.08 / 2.0;
}

printf("%.2f",height);



return 0;
}

