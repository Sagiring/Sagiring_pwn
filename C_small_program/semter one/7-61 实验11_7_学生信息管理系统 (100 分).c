#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct student {
	int is;
	char num[11];
	char name[11];
	int  score[3];
} stu; 
int equal(struct student a,struct student b);
int main() {
	int function=0,exit=0;
	int n;
	scanf("%d",&n);
	stu stu_dent[n];
	getchar();
	for(int i=0; i<n; i++) {
		stu_dent[i].is=0;
	}
	for(int x=0; x<n; x++) {
		exit=0;
		function=-1;
		scanf("%d",&function);

		switch (function) {

			case 1: {

				stu a;
				scanf("%s",a.num);
				scanf("%s",a.name);
				//输入 学号 姓名
				for(int i=0; i<3; i++) {
					scanf("%d",&a.score[i]);
				}
				//输入 成绩
				//查找 功能

				for(int i=0; i<n; i++) {
					//查重功能↓
					if(stu_dent[i].is==1) {
						if(equal(a,stu_dent[i])==1) {
							exit=1;
							printf("Students already exist\n");
						}
					}
					if(exit==1) {
						break;
					}
					//查重功能↑
				}
				//入库功能↓
				if(exit==0) {
					for(int i=0; i<n; i++) {
						if(stu_dent[i].is==0) {
							stu_dent[i]=a;
							printf("Add success\n");
							stu_dent[i].is=1;
							break;
						}
					}
				}
				break;
			}
			case 2: {

				stu a;
				scanf("%s",a.num);
				for(int i=0; i<n; i++) {
					if(stu_dent[i].is==1) {
						if(strcmp(stu_dent[i].num,a.num)==0) {

							stu_dent[i].is=0;
							//删除功能↑
							printf("Delete success\n");
							exit=1;
							break;
						}
					}
				}
				if(exit==0) {
					printf("Students do not exist\n");
				}

				break;
			}
			case 3: {
				stu a;
				scanf("%s",a.num);

				for(int i=0; i<3; i++) {
					scanf("%d",&a.score[i]);
				}

				for(int i=0; i<n; i++) {
					if(stu_dent[i].is==1) {
						if(strcmp(stu_dent[i].num,a.num)==0) {

							a.is=1;
							strcpy(a.name,stu_dent[i].name);
							stu_dent[i]=a;
							//更新数据↑

							printf("Update success\n");
							exit=1;
							break;
						}
					}
				}
				if(exit==0) {
					printf("Students do not exist\n");
				}

				break;
			}


			case 4: {
				stu a;
				double average=0.0;
				scanf("%s",a.num);
				for(int i=0; i<n; i++) {
					if(stu_dent[i].is==1) {
						if(strcmp(stu_dent[i].num,a.num)==0) {
							for(int cnt=0; cnt<3; cnt++) {
								average+=stu_dent[i].score[cnt];
							}
							exit=1;
							average/=3.0;
							printf("Student ID:%s\n",stu_dent[i].num);
							printf("Name:%s\n",stu_dent[i].name);
							printf("Average Score:%.1f\n",average);
							break;
						}
					}
				}
				if(exit==0) {
					printf("Students do not exist\n");
				}

				break;
			}


		}





	}
	return 0;
}
int equal(struct student a,struct student b) {
	int is=0,result;
	result=strcmp(a.num,b.num);
//	if(result==0) {
//		result=strcmp(a.name,b.name);
//		if(result==0) {
//			for(int i=0; i<3; i++) {
//				if(a.score[i]!=b.score[i]) {
//					result=1;
//				}
//			}
			if(result==0) {
				return 1;
			}
//		}
//	}
	return 0;
}

