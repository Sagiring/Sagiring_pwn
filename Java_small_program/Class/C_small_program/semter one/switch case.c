#include <stdio.h>

int main(){
int a,b,c;

char d;
scanf("%d %c %d",&a,&d,&b);

switch (d){
	case '+':
		c=a+b;
		break;
	case '-':
		c=a-b;
		break;
	case '/':
	    c=a/b;
	    break;
	case '*':
	    c=a*b;
		break;
	case '%':
		c=a%b;
		break;
	default:
	printf("ERROR");
	goto out;	
}
printf("%d",c);

out:
	return 0;
}
