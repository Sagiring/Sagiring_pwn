
#include<stdio.h>

#define        LEN        100

//��������
void distribute(int * bullets , int size , int number ) ;

int main() {
	int        bullets[LEN] ;
	int        n , m , i ;

	scanf("%d" , &n ) ;    //����սʿ����
	for( i = 0 ; i < n ; i++ ) {
		scanf("%d" , &bullets[i] ) ;//����ÿ��սʿ���г�ʼ���ӵ���
	}
	scanf("%d" , &m ) ;//��������Ĵ�����m>0)

	distribute(bullets , n , m ) ;//����

	for( i = 0 ; i < n - 1 ; i++ ) { //�����������
		printf("%d " , bullets[i] ) ;
	}
	printf("%d\n" , bullets[i] ) ;

	return 0;
}


/* ����������д�� */
void distribute(int * bullets , int size , int number ) {

	for(int i=0; i<number; i++) {
		for(int x=0; x<size; x++) {

			if(bullets[x]%2==1) {
				bullets[x]++;
			}
			bullets[x]/=2;
		}
	int tem[size];
	for(int i=0;i<size;i++){
		tem[i]=bullets[i];
	}
		for(int cnt=0; cnt<size; cnt++) {
			if(cnt+1==size) {
				bullets[0]+=tem[cnt];
			} else {

				bullets[cnt+1]+=tem[cnt];

			}
		}
	}




}
