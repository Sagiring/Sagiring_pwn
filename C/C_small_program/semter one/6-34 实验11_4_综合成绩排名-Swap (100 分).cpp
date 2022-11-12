#include <stdio.h>

typedef struct
{
    char    id[16]  ;//ѧ���˺� 
    int        total ;    //�ۺϳɼ� 
    int        ce ;    //���Գɼ� 
    int        ws ;    //��Ȩ�ɼ� 
}STUDENT;

void Sort(STUDENT a[],int size) ; 
void Swap(STUDENT * s1,STUDENT * s2) ;
int  Comp(STUDENT * s1,STUDENT * s2) ;

int main()
{
    STUDENT    stu[100] ;
    int        i , n ;


    scanf("%d",&n) ;
    for(i=0;i<n;i++)
    {
        scanf("%s%d%d",stu[i].id,&stu[i].ce,&stu[i].ws) ;
        stu[i].total = stu[i].ce+stu[i].ws ;
    }

    Sort(stu,n) ;
    for(i=0;i<n;i++)
        printf("%s %d %d %d\n",stu[i].id,stu[i].total,stu[i].ce,stu[i].ws) ;

    return 0;    
}


//�����д��ֻ��ʵ���±���һ������������������������ʵ�֣������ӿ����£�
void Swap(STUDENT * s1,STUDENT * s2) {
	STUDENT c={0,0,0,0};
	c=*s1;
	*s1=*s2;
	*s2=c;
	
}
//�����д��ֻ��ʵ���±���һ������������������������ʵ�֣������ӿ����£�
int  Comp(STUDENT * s1,STUDENT * s2)  {
	if((s1->total)>(s2->total)){
		return 1;
	}else if((s1->total)<(s2->total)){
		return 0;
	}else if((s1->total)==(s2->total)){
		if((s1->ce)>(s2->ce)){
			return 1;
		}else{
			return 0;
		}
	}
	
}
//�����д��ֻ��ʵ�ֵ�����������ʵ�ִ˺���ʱ����ֱ�ӵ����������������������������ӿ����£�
void Sort(STUDENT a[],int size) {
	int is=3;
	for(int cnt=1;cnt<size-1;cnt++)
	for(int i=0;i<size-cnt;i++){
		is= Comp(&a[i],&a[i+1]);
		if(is==0){
			Swap(&a[i],&a[i+1]);
		}	
	}
	
	
	
	
	
}
