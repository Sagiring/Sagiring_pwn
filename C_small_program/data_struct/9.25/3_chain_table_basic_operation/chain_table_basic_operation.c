#include <stdio.h>
#include <stdlib.h>
typedef struct link
{
    int elem;
    struct link *next;
} link;

link *InitList(int size_num)
{
    link *head = NULL;
    link *tem = (link *)malloc(sizeof(link));
    tem->elem = 0;
    tem->next = NULL;
    head = tem;
    for (int i = 0; i < size_num; i++)
    {
        link *new = (link *)malloc(sizeof(link));
        new->elem = i + 1;
        new->next = NULL;
        tem->next = new;
        tem = tem->next;
        // 转换到new对象
    }
    return head;
}

void free_list(link *p)
{
    link *tem = p;
    link *next = p->next;
    while (next)
    {
        free(tem);
        tem = next;
        next = next->next;
    }
    free(tem);
}

link *insert_loc_list(link *head, link *p, int loc)
{
    if (loc == 1)
    {
        link *tem = (link *)malloc(sizeof(link));
        tem = head->next;
        head->next = p;
        p->next = tem;
        return p;
    }
    else
    {
        link *tem = NULL;
        link *elem = (link *)malloc(sizeof(link));
        elem = head->next;
        for (int i = 1; i < loc - 1; i++)
        {
            elem = elem->next;
        }
        tem = elem->next;
        elem->next = p;
        p->next = tem;

        return p;
    }
}

void print_list(link *head)
{
    printf("List->");

    link *tem = head->next;
    while (tem->next)
    {
        printf("%d,", tem->elem);
        tem = tem->next;
    }
    printf("%d.\n", tem->elem);
}

int find_elem(link *head, int loc)
{
    if (loc == 1)
    {
        return head->next->elem;
    }
    else
    {
        link *elem = head->next;
        for (int i = 1; i < loc - 1; i++)
        {
            elem = elem->next;
        }
        return elem->elem;
    }
}

int main()
{
    link *l;
    link *p;
    p = (link *)malloc(sizeof(link));
    p->elem = 10;
    p->next = NULL;
    // 生成插入节点
    int loc;
    int size_num = 5;
    l = InitList(size_num);
    // 链表生成 自动填充{1，2，3......,n}
    printf("要插入的位置是{0,1,..,n}>");
    scanf("%d", &loc);
    if (size_num + 1 >= loc && loc > 0)
    {
        insert_loc_list(l, p, loc);
        // 链表插入操作
        print_list(l);
        // 链表遍历print
    }
    else
    {
        printf("位置不合法\n");
    }

    printf("要删除的位置是{1,2,...,n}>");
    scanf("%d", &loc);
    if (size_num  >= loc && loc > 0)
    {
        delete_loc_list(l, loc);
        // 链表删除节点并且释放操作
        print_list(l);
        // 链表遍历print
    }
    else
    {
        printf("位置不合法\n");
    }

    printf("要查询的位置是{1,2,...,n}>");
    scanf("%d", &loc);
    if (size_num  >= loc && loc > 0)
    {
        printf("该位置的值为>%d\n",find_elem(l, loc+1));
        // 链表插入操作
    }
    else
    {
        printf("位置不合法\n");
    }

    print_list(l);
    // 链表遍历print
    free_list(l);
    // 链表全部释放操作

    return 0;
}