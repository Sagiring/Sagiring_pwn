//���������õ��������£�

#include<stdio.h>

//ѡ���������� 
//����˵�������飬����������Ԫ�ظ��� 
void selectSort(int data[],int elementCount) ;

//�������ܣ��������е���СֵԪ�أ����������±� 
//����˵������������������ʼλ���±꣬������ֹλ���±�
int findMin(int data[], int startLoc, int endLoc) ; 

//�������������Ԫ�� 
//����˵�������飬����������Ԫ�ظ��� 
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

