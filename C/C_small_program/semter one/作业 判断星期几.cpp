#include <stdio.h>

#include<math.h>

int daycnt(int a,int b,int c);


int main() {

	int a,b,c,day,result,x;

	printf("������������2002 11 23\n");
	scanf("%d %d %d",&a,&b,&c);

	day=daycnt(a,b,c);
	result=day%7;

	if(a>2021||(a==2021&&b>10)||(a==2021&&b==10&&c>=28)){
		x=1;
	}else{
		x=0;
	}

	if(x==0) {


		switch (result) {

			case 1:
				printf("������");
				break;
			case 2:
				printf("���ڶ�");
				break;
			case 3:
				printf("����һ");
				break;
			case 4:
				printf("������");
				break;
			case 5:
				printf("������");
				break;
			case 6:
				printf("������");
				break;
			case 0:
				printf("������");
		}
	}else if(x==1) {

		switch (result) {
			case 1:
				printf("������");
				break;
			case 2:
				printf("������");
				break;
			case 3:
				printf("������");
				break;
			case 4:
				printf("����һ");
				break;
			case 5:
				printf("���ڶ�");
				break;
			case 6:
				printf("������");
				break;
			case 0:
				printf("������");
		}
	}


	return 0;
}

int daycnt(int a,int b,int c) {
	int result;
	int cnt;

//	result+=365*abs(a-2021); �������� 
	
	

	if(a<=2021) {

		for(cnt=a; cnt!=2021; cnt++) {
			if((cnt%4==0&&cnt%100!=0)||cnt%400==0) {
				result++;
			}
		}
	} else {
		for(cnt=a; cnt!=2021; cnt--) {
			if((cnt%4==0&&cnt%100!=0)||cnt%400==0) {
				result++;
			}
		}
	}


	b=12-b;

	switch (b) {
		case 0:
			result+=31+30;
			break;
		case 1:
			result+=30;
			break;
		case 2:
			result+=0;
			break;
		case 3:
			result+=31+30+31;
			break;
		case 4:
			result+=30+31+30+31;
			break;
		case 5:
			result+=31+30+31+30+31;
			break;
		case 6:
			result+=31+31+30+31+30+31;
			break;
		case 7:
			result+=30+31+31+30+31+30+31;
			break;
		case 8:
			result+=31+30+31+31+30+31+30+31;
			break;
		case 9:
			result+=30+31+30+31+31+30+31+30+31;
			break;
		case 10:
			result+=31+30+31+30+31+31+30+31+30+31;
			break;
		case 11:
			result+=28+31+30+31+30+31+31+30+31+30+31;
			if((a%4==0&&a%100!=0)||a%400==0) {
				result++;
			}
			break;
	}



	if(c<=28) {
		result+=28-c;
	} else {
		result+=c-28;
	}




	return result;
}
