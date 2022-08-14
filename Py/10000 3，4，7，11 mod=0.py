sum=0
for i in range(1,10001):
    # print(i)
    if(i%3!=0 and i%4!=0 and i%7!=0 and i%11!=0):
        sum+=1
    print(sum)    