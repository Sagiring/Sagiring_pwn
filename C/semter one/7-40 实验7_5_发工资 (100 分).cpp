#include <stdio.h>
int main() {
	int piece;
	int money[]= {100,50,20,10,5,2,1,} ;
	int salary;
	scanf("%d",&salary);
	for(int i=0; i<sizeof(money)/sizeof(money[0])&&salary!=0; i++) {
		piece=salary/money[i];
		if(piece!=0) {

			printf("%d:%d\n",money[i],piece);
		}
		salary=salary-piece*money[i];
	}





	return 0;
}

