//���������ý��в��Ե��������£�
#include<stdio.h>

int getString( char * source , char *strPtr[] ) ;

int main() {
	char    str[100];
	char    *strPtr[50]= {0};
	int        i, num ;

	gets(str);
	num = getString( str , strPtr ) ;
	for( i = 0 ; i < num ; i++ )
		puts(strPtr[i]);

	return 0;
}

/* ����������д�� */
//����ԭ�����£�
int getString( char * source , char *strPtr[] ) {
	int i,num=0,cnt=0,is=1;
	if(source[0]!=' ') {
		strPtr[cnt]=&source[0];
		cnt++;
		is=0;
		num++;
	}
	for(i=1; source[i]!='\0'; i++) {
		if(source[i]==' ') {
			source[i]='\0';
			i++;
			while(source[i]==' ') {
				i++;
			}
			if(source[i]!='\0') {
				is=1;
			}
		}
		if(is==1) {
			strPtr[cnt]=&source[i];
			cnt++;
			is=0;
			num++;
		}
	}
	return num;
}
