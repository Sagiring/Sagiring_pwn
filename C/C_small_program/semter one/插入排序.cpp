//���������õ��������£�
#include<stdio.h>

//������������
//����˵�������飬����������Ԫ�ظ���
void InsertSort(int a[],int n);

int main() {
	int        n , i,    num[1000] ;

	scanf( "%d" , &n );
	for( i = 0 ; i < n ; i++ )
		scanf( "%d", &num[i] ) ;
	InsertSort( num , n ) ;
	return 0 ;
}

/* ����������д�� */
//����ԭ�����£�

void InsertSort(int a[],int n) {
	int c;
	for(int i=1; i<n; i++) {

		for(int cnt=0; cnt<i; cnt++) {
			c=a[i];
			if(a[i]>=a[cnt]&&a[i]<=a[cnt+1]) {

				for(int x=i; x>cnt; x--) {
					a[x]=a[x-1];
				}
				a[cnt+1]=c;
			} else if(a[i]<a[0]) {
					for(int x=i; x>0; x--) {
					a[x]=a[x-1];
				}
				
				a[0]=c;
			
			}



		}
		for(int i=0; i<n-1; i++) {
			printf("%d ",a[i]);
		}
		printf("%d\n",a[n-1]);
	}

}
