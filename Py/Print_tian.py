



def print_tian(n):
    for k in range(0,n):
        print("+",end="")
        for i in range(0,n):
            print("----+",end="")
        # 上面是有+号的打印

        print("\r")
        
        for i in range(0,4):
            for j in range(0,n):    
                print("|    ",end="")
            print("|")
        # 上面是无加号行的打印

    print("+",end="")
    for i in range(0,n):
        print("----+",end="")
    # 上面是最后一行的打印


print("请输入n=",end="")
n=int(input())
print_tian(n)

