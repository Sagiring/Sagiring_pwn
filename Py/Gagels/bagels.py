import random
import os
import time


def main():
    All_Digits ='0123456789'
    Max_Try = 20
    Num_Digits = 3

    os.system('cls')
    print(f'我想好了一个{Num_Digits}位不重复的数字，你来猜猜看！')

    

    target = ''.join(random.sample(All_Digits, k=Num_Digits))
    round=1
    start_time = int(time.time())

    while 1:
        guess = user_input(Num_Digits)

        if guess == target:
            print('-----Win!-----')
            end_time = int(time.time())
            user_time = end_time-start_time
            print(f'总共猜了{round}次,用时{end_time-start_time}秒')
            write_user_time_list(user_time)
            print_user_time_list()
            break
        else:
            print(get_glue(target, guess))

        if round >= Max_Try:
            print(f'你已经猜了{round}次,游戏失败')
            break
        round += 1

def write_user_time_list(user_time):
    user_name = input('请输入你的用户名称->')
    with open('E:\Study\Py\Gagels\second_list.txt','a+') as f:
        f.write(f'用户名称 {user_name} 所用时间 {user_time} ')
        f.write('\n')
        
def print_user_time_list():


    with open('E:\Study\Py\Gagels\second_list.txt') as f:
            context = f.read()
            print('---排行榜排名---')

        
            user_list = []
            user_text = context.split('\n')
            for user_info in user_text[:-1]:
                user_data = user_info.split(' ')
                # print(user_data)
                uid = user_data[1]
                user_time = user_data[3]
                
                user_list.append([uid,int(user_time)])
            user_list.sort(key= lambda x:x[1])
            # 未弄懂的函数
            # 整理排行榜数据

            # 排行榜去重 待优化的代码
            is_first = 1
            is_double = 0
            is_exit = 0
            for user_info in user_list:
                    if is_first:
                            double_name = [[user_info[0],user_info[1]]]
                            is_first = 0
                    
                    for cnt in range(0,len(double_name)):
                            if user_info[0] in double_name[cnt]:
                                    is_double = 1
                                    # print(double_name)
                                    for i in range(0,len(double_name)):
                                            if user_info[0] == double_name[i][0]:    
                                                    if user_info[1] < double_name[i][1]:
                                                            double_name[i][1] = user_info[1]
                                                            is_exit = 1
                                                            break
                    if is_exit:
                        is_exit = 0
                        break                                        
                    
                    if not is_double:
                            double_name.append([user_info[0],user_info[1]])
                    is_double = 0

            for user_info in double_name:
                print(f'player>{user_info[0]}---耗时>{user_info[1]}s')
       
def user_input(Num_Digits):
    while 1:
        guess = input('> ')
            #isdigit判读是否为数字
            # 利用集合不重复的性质去重 
        if len(guess) == Num_Digits\
                and len(guess) == len(set(guess)) \
                and guess.isdigit():
            break
        else:
            print(f'请输入{Num_Digits}位不重复的数字')
    return guess


def get_glue(target, guess):
    glue = ''
    for index in range(len(guess)):
        if guess[index] == target[index]:
            glue += ' ✔'
        elif guess[index] in target:
            glue += ' ⭕'
        else:
            glue += ' ❌'
            # glue = ''.join(sorted(list(glue)))
            # 打乱字符
    return glue


main()