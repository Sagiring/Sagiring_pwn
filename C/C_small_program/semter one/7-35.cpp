#include <stdio.h>
#include <math.h>
int main() {

	double x,ex=1.0,xiang=1.0,jc=1.0;
	scanf("%lf",&x);
	if(fabs(x)<1e-6) {
		ex=1.0;
	} else {

		for(int i=1; fabs(xiang)>1e-8; i++) {


				jc=i*jc;

			xiang=pow(x,i)/jc;
			ex+=xiang;
		}
	}
printf("%.4f",ex);


	return 0;
}

