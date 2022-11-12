//设计了辅助函数后，函数被调用的例子如下：
#include<stdio.h>

void bubbleSort(int a[],int n);

//输出数组中所有元素 
void outputData(int data[],int elementCount) ;

int main()
{
    int        n , i,    num[10010] ;

    scanf("%d",&n); 
    for( i = 0 ; i < n ; i++ ) 
        scanf("%d",&num[i]) ;
    bubbleSort(num,n) ; 
    outputData(num,n) ;
    return 0 ;
}
//注：此题大家可以练习各种排序算法。
//函数原型如下：
void bubbleSort(int a[],int n){
	int c;
	for(int cnt=n-1;cnt>0;cnt--){
	
	for(int i=0;i<cnt;i++){
		if(a[i]>a[i+1]){
			c=a[i];
			a[i]=a[i+1];
			a[i+1]=c;
		}
	}
}
	
	
}
//辅助函数原型：
void outputData(int data[],int elementCount) {
	for(int i=0;i<elementCount-1;i++){
		printf("%d ",data[i]);
	}
	printf("%d\n",data[elementCount-1]);
}

/* 请在这里填写答案 */
