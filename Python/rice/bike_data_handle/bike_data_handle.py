import pandas as pd
import matplotlib.pyplot as plt

    
def read_dataframe():
    with open("./data/bike_day.csv",'r') as f:
        data = pd.read_csv(f)
    # 读取
        print(pd.concat([data[:5],data[len(data)-2:]]))
    #查看前5行、后两行 
        print("1) complete!")
    return data


def writeIn_userTxt(data):
    data_instant = data["instant"]
    data_dteday = data["dteday"]
    data_weekday = data["weekday"]
    data_casual = data["casual"]
    data_registered = data["registered"]
    with open("./data/bike_weekday_user.txt",'w',encoding="utf-8") as f:
        for i in range(0,len(data_instant)):
            if(data_instant[i] and data_dteday[i] and data_weekday[i] in range(0,7) and data_casual[i] and data_registered[i]):
                # 判断是否满足数据要求
                write_in = f"{data_instant[i]} {data_dteday[i]} {data_weekday[i]} {data_casual[i]} {data_registered[i]}\n"
                f.write(write_in)
        # 写入到user.txt
    print("2) complete!")

def writeIn_cnt():
    with open("./data/bike_weekday_user.txt",'r',encoding="utf-8") as f:
        with open("./data/bike_weekday_user_cnt.xlsx",'w',encoding="utf-8") as g:
            data = f.read().split("\n")
            for i in data:
                tem = i.split(" ")
                if(i):
                    cnt = int(tem[len(tem)-2]) + int(tem [len(tem)-1])
                    # 计算cnt
                    write_in  = f"{i} {cnt}\n"
                    g.write(write_in)
    print("3) complete!")

def averageCnt_week():
    cnt_sum = [0,0,0,0,0,0,0] #存放总和值
    cnt_num = [0,0,0,0,0,0,0] #存放总和个数
    num = 0
    with open("./data/bike_weekday_user_cnt.xlsx",'r',encoding="utf-8") as f:
        with open("./data/bike_weekday_user_cnt_mean.txt",'w',encoding="utf-8") as g:
            data = f.read().split("\n")
            for i in data[:-1]:
                tem = i.split(" ")
                # 进行遍历
                cnt_sum[int(tem[2])] +=int(tem[-1])
                cnt_num[int(tem[2])] += 1
            # print(cnt_sum,cnt_num)
            for i in range(0,7):
                average = cnt_sum[i] / cnt_num[i]
                # 计算平均值
                write_in  = f"{num},{average}\n"
                g.write(write_in)
                num+=1
    print("4) complete!")

def toView_cnt():
    list_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    with open("./data/bike_weekday_user_cnt_mean.txt",'r',encoding="utf-8") as f:
        data = f.read().split("\n")
    list_data = []
    for i in data[:-1]:
        tem = i.split(",")
        list_data.append(int(float(tem[1])))
    df = pd.DataFrame(list_week,columns=["weekday"])
    df["user_cnt"] = list_data
    # print(df)
    # 创建dataFrame

    yticks = [] #创建纵坐标表
    for i in range(0,21):
        yticks.append(i * 250)
    df.plot(x='weekday', y='user_cnt', kind='bar',title ="bike_day_user_cnt",figsize=(10, 10))
    plt.yticks(yticks)
    plt.savefig('./bike_day_user_cnt.png')
    # 生成图片
    print("5) complete!")



def main():
    try:
        data = read_dataframe()
        # 检查是否有数据集文件
    except(FileNotFoundError):
        print("No data_file ,check plz")
        exit(1)
    writeIn_userTxt(data) 
    writeIn_cnt()
    averageCnt_week()
    toView_cnt()
main()

