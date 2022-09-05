#include <stdio.h>
int main() {
	int n,sum=0,is=0,result=0;
	scanf("%d",&n);
	char a[19];
	getchar();
	for(int cnt=0; cnt<n; cnt++) {
		
		gets(a);
for(int i=0;i<18;i++){
	a[i]-='0';
}
		sum=(a[0]*7)+(a[1]*9)+(a[2]*10)+(a[3]*5)+(a[4]*8)+(a[5]*4)+(a[6]*2)+(a[7]*1)+(a[8]*6)+(a[9]*3)+(a[10]*7)+(a[11]*9)+(a[12]*10)+(a[13]*5)+(a[14]*8)+(a[15]*4)+(a[16]*2);

		is=sum%11;
		switch (is) {
			case 0:
				result=1;
				break;
			case 1:
				result=0;
				break;
			case 2:
				result='X'-'0';
				break;
			case 3:
				result=9;
				break;
			case 4:
				result=8;
				break;
			case 5:
				result=7;
				break;
			case 6:
				result=6;
				break;
			case 7:
				result=5;
				break;
			case 8:
				result=4;
				break;
			case 9:
				result=3;
				break;
			case 10:
				result=2;
				break;
		}

		if(result==a[17]) {
			printf("right\n");
		} else {
			printf("wrong\n");
		}


	}

	return 0;
}

