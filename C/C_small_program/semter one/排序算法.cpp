//����˸��������󣬺��������õ��������£�
#include<stdio.h>

void bubbleSort(int a[],int n);

//�������������Ԫ�� 
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
//ע�������ҿ�����ϰ���������㷨��
//����ԭ�����£�
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
//��������ԭ�ͣ�
void outputData(int data[],int elementCount) {
	for(int i=0;i<elementCount-1;i++){
		printf("%d ",data[i]);
	}
	printf("%d\n",data[elementCount-1]);
}

/* ����������д�� */
