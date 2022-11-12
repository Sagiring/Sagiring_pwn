#include<stdio.h>

int main() {
	int ru,ru2, i;

	scanf_s("%d", &ru);

	for (i = 0; i>5; i++)
	{
		ru2 = ru % 10;
		ru2 = ru2 + (ru % 10) * 10 * i;
		ru = ru / 10;
		printf("%d", ru2);
	}





	return 0;
}