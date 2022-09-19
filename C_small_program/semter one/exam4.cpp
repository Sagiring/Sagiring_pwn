#include <stdio.h>
int main() {
	int i;
	scanf("%d",&i);
//ĞĞÊı
	int year,cnt;

	for(; i!=0; i--) {

			cnt=0;
		do {
			
			scanf("%d",&year);

			if((year%4==0&&year%100!=0)||year%400==0) {
				cnt++;
			}

		}while(year!=-1);
		
		printf("%d\n",cnt);

	}
	return 0;
}
