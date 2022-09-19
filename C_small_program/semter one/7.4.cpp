#include <stdio.h>

int change(char start){
	switch (start){
		case '1':
			start=1;
			break;
		case '2':
			start=2;
			break;
		case '3':
			start=3;
			break;
		case '4':
			start=4;
			break;
		case '5':
			start=5;
			break;	
		case '6':
			start=6;
			break;
		case '7':
			start=7;
			break;
		case '8':
			start=8;
			break;
		case '9':
			start=9;
			break;
		case 'T':
			start=10;
			break;		
   		
	}
	
	  return start;
}


int main(){
char start;
int a=0,b=0,result=2,i,c1,c2;
//¿ÉÒÔĞ´maxº¯Êı 
int x[2],y[2];

for(i=0;i<2;i++){
scanf("%c",&start);

start=change(start);
x[i]=start;
a+=start;
a%=10;
}
for(i=0;i<2;i++){
scanf("%c",&start);
start=change(start);
y[i]=start;
b+=start;
b%=10;
}
//printf("a=%d b=%d",a,b);
c1=x[0];
c2=y[0];
//µ¥ÅÆÅĞ¶Ï 
if(a>b){
	result=1;
}else if(a<b){
	result=0;
}else if(a==b){
	for(i=0;i<2;i++){
		if(x[0]<x[1]){
			c1=x[1];
		}
		if(y[0]<y[1]){
			c2=y[1];
		}
	}
	if(c1>c2){
		result=1;
	}else if(c1<c2){
		result=0;
	}else if(c1==c2){
	result=2; 
	}	
}
//¶Ô×ÓÅĞ¶Ï 
if(x[0]==x[1]&&y[0]!=y[1]){
	result=1;
}else if(x[0]!=x[1]&&y[0]==y[1]){
	result=0;
}else if(x[0]==x[1]&&y[0]==y[1]){
	if(x[0]>y[0]){
		result=1;
	}else if(x[0]<y[0]){
		result=0;
	}else if(x[0]==y[0]){
		result=2;
	}
}
//Êä³öÅĞ¶Ï 
if(x[0]!=x[1]&&y[0]!=y[1]){

switch (result){
	case 0:
		printf("B:%d",b);
		break;
	case 1:
		printf("A:%d",a);
		break;
	case 2:
		printf("A:%d",a);
		break;
		
}
	
}else if((x[0]==x[1]||y[0]==y[1])&&x[0]!=10&&y[0]!=10){
	switch (result){
	case 0:
		printf("B:%d",y[0]);
		break;
	case 1:
		printf("A:%d",x[0]);
		break;
	case 2:
		printf("A:%d",x[0]);
		break;
}
}else if((x[0]==x[1]||y[0]==y[1])&&(x[0]==10||y[0]==10)){
	switch (result){
	case 0:
		printf("B:T");
		break;
	case 1:
		printf("A:T");
		break;
	case 2:
		printf("A:T");
		break;
}	
}

return 0;
}

