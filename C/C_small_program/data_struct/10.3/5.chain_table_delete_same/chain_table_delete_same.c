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

int find_delete_list_same(link *head, int loc, int size)
{
    int data = 0;
    int delete_loc = -1;
    link *elem = head->next;
    if (loc == 1)
    {
        data = head->next->elem;
        for (int i = 1; i < size - 1; i++)
        {
            elem = elem->next;
            if (data == elem->elem)
            {
                delete_loc = i + 1;
            }
        }
    }
    else
    {

        for (int i = loc; i < size - 1; i++)
        {
            elem = elem->next;
        }
        data = elem->elem;

        for (int i = loc + 1; i < size - 1; i++)
        {
            if (elem->next)
            {
                elem = elem->next;
            }
            else
            {
                break;
            }
            if (data == elem->elem)
            {
                delete_loc = i;
            }
        }

        return delete_loc;
    }
}

link *delete_loc_list(link *head, int loc)
{
    if (loc == 1)
    {
        link *tem = NULL;
        tem = head->next;
        head->next = head->next->next;
        free(tem);
        return head;
    }
    else
    {
        link *tem = NULL;
        link *elem = head->next;
        for (int i = 1; i < loc - 1; i++)
        {
            elem = elem->next;
        }
        tem = elem->next;
        elem->next = elem->next->next;
        free(tem);
        return elem;
    }
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

int main()
{
    link *l;
    link *p;
    p = (link *)malloc(sizeof(link));
    p->elem = 3;
    p->next = NULL;
    // 生成插入节点
    int loc;
    int size_num = 5;
    l = InitList(size_num);
    // 链表生成 自动填充{1，2，3......,n}

    print_list(l);
    // 链表遍历print
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
    printf("进行除重操作\n");
    for (int i = 0; i < size_num - 1; i++)
    {
        loc = find_delete_list_same(l, i, size_num);
        if (loc != -1)
        {
            delete_loc_list(l, loc);
        }
    }

    print_list(l);
    // 链表遍历print
    free_list(l);
    // 链表全部释放操作

    return 0;
}