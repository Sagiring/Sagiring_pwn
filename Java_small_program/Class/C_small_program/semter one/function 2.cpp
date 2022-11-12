//函数被调用的例子如下：
#include<stdio.h>

int    getDays(int,int) ;

int main() {
	int    year, month ;

	scanf("%d%d",&year,&month);
	printf("There are %d days in month %d year %d.",getDays(year,month), month, year) ;

	return 0 ;
}

/* 请在这里填写答案 */
int    getDays(int year,int month) {
	int isrun=0,day=0;

	if (year%400==0||(year%4==0&&year%100!=0)) {
		isrun=1;
	}
	switch (month) {
		case 1:
			day=31;
			break;
		case 2:
			day=28;
			break;
		case 3:
			day=31;
			break;
		case 4:
			day=30;
			break;
		case 5:
			day=31;
			break;
		case 6:
			day=30;
			break;
		case 7:
			day=31;
			break;
		case 8:
			day=31;
			break;
		case 9:
			day=30;
			break;
		case 10:
			day=31;
			break;
		case 11:
			day=30;
			break;
		case 12:
			day=31;
			break;
	}
if(month==2&&isrun==1){
	day++;
}
return day;
}
