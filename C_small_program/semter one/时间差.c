#include <stdio.h>
#include<stdlib.h>
int main()
{
	int hour1=0,minute1=0;

	printf("请输入较晚时间,如14点35分输入14 35\n");
	scanf("%d %d",&hour1,&minute1);
	
	printf("请输入较早时间,如7点0分 输入7 0\n");
	int hour2=0,minute2=0;
	scanf("%d %d",&hour2,&minute2);
	
	int minute3=(hour1*60+minute1)-(hour2*60+minute2);
	double hour3=minute3/60.0;
	
	printf("小时差：%f,分钟差：%d\n",hour3,minute3);
	
	int minute4=minute3%60;
	int hour4=minute3/60 ;
	
	printf("\n共计差%d小时%d分钟\n",hour4,minute4);
	
	
	 system("pause");
	 
	
	
	
	
	
	
	
	
	return 0;
}

