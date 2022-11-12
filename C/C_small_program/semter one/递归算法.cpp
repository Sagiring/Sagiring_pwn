#include <stdio.h>
void hanoi(int num, char source, char target,char auxiliary) {
    //ͳ���ƶ�����
    static int i = 1;
    //���Բ���������� 1 ������ֱ�Ӵ���ʼ���ƶ���Ŀ����
    if (num == 1) {
        printf("��%d��:�� %c �ƶ��� %c\n", i, source, target);
        i++;
    }
    else {
        //�ݹ���� hanoi() �������� num-1 ��Բ�̴���ʼ���ƶ�����������
        hanoi(num - 1, source, auxiliary, target);
        //����ʼ����ʣ������һ����Բ���ƶ���Ŀ������
        printf("��%d��:�� %c �ƶ��� %c\n", i, source, target);
        i++;
        //�ݹ���� hanoi() ���������������ϵ� num-1 Բ���ƶ���Ŀ������
        hanoi(num - 1, auxiliary, target, source);
    }
}

int main()
{
    //���ƶ� 3 ��Բ��Ϊ������ʼ����Ŀ�������������ֱ��� A��B��C ��ʾ
    hanoi(4, 'A', 'B', 'C');
    
    return 0;
}
