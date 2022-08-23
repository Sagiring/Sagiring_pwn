from ast import Num
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
        while 1:
            guess = input('> ')
            #isdigit判读是否为数字
            if len(guess) == Num_Digits\
                and len(guess) == len(set(guess)) \
                and guess.isdigit():
                break
            else:
                print(f'请输入{Num_Digits}位不重复的数字')

        if guess == target:
            print('-----Win!-----')
            end_time = int(time.time())
            print(f'总共猜了{round}次,用时{end_time-start_time}秒')
            break
        else:
            print(get_glue(target, guess))

        if round >= Max_Try:
            print(f'你已经猜了{round}次,游戏失败')
            break
        round += 1


def get_glue(target, guess):
    glue = ''
    for index in range(len(guess)):
        if guess[index] == target[index]:
            glue += ' ✔'
        elif guess[index] in target:
            glue += ' ⭕'
        else:
            glue += ' ❌'
            glue = ''.join(sorted(list(glue)))
    return glue


main()