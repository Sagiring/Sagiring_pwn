//1784
#include <stdio.h>

int main()
{
	double R=0;
	double c=0;
	double area=0;
	const double PI=3.14159265;
	scanf("%lf",&R);
	
	c=2*PI*R;
	area=PI*R*R;
	
	printf("The perimeter is %.4lf, the area is %.4lf\n",c,area);
	
	
	
	return 0;
}
