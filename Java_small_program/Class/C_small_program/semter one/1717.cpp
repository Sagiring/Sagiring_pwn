#include <stdio.h>

int main(){
int score;

scanf("%d",&score);

if(score<=100&&score>=90){
	printf("A");
}else if(80<=score&&score<90){
	printf("B");
}else if(70<=score&&score<80){
	printf("C");
}else if(60<=score&&score<70){
	printf("D");
}else if(score<60){
	printf("E");
}else{
	printf("The score is out of range!");
}
	
	
	
	
	
	
	
	
	
	
	return 0;
}
