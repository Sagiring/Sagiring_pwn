//函数被调用的例子如下：

#include<stdio.h>

//选择排序（升序） 
//参数说明：数组，数组中已有元素个数 
void selectSort(int data[],int elementCount) ;

//函数功能：找数组中的最小值元素，并返回其下标 
//参数说明：数组名，查找起始位置下标，查找终止位置下标
int findMin(int data[], int startLoc, int endLoc) ; 

//输出数组中所有元素 
//参数说明：数组，数组中已有元素个数 
void outputData(int data[],int elementCount) ;

int main()
{
    int        n , i,    num[1010] ;

    scanf("%d",&n); 
    for( i = 0 ; i < n ; i++ ) 
        scanf("%d",&num[i]) ;
    selectSort(num,n) ; 
    return 0 ;
}


void selectSort(int data[],int elementCount) {
	int Loc=0,c;
	for(int i=0;i<elementCount-1;i++){
		Loc=findMin(data,i,elementCount-1);
		c=data[Loc];
		data[Loc]=data[i];
		data[i]=c;
		outputData(data,elementCount);
	}
}


int findMin(int data[], int startLoc, int endLoc) {
	int min=data[startLoc];
	int Loc=startLoc;
	for(int i=startLoc;i<=endLoc;i++){
		if(data[i]<min){
			min=data[i];
			Loc=i;
		}
	}
	return Loc;
}


void outputData(int data[],int elementCount) {
			for(int cnt=0; cnt<elementCount-1; cnt++) {
			printf("%d ",data[cnt]);
		}
		printf("%d\n",data[elementCount-1]);
	}

