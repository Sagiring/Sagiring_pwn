import random
import time


def lottery_1(u_list):
    select_user_info = random.choice(u_list).split()
    print(f"恭喜中奖用户{select_user_info[0]} {select_user_info[1]}")
    return select_user_info[0]
    
def lottery_2(u_list):
    while 1:
        try:
            idx = int(time.time() * 1000) % len(u_list)
            print(f'\r{u_list[idx]}',end='')
            time.sleep(0.001)
        except KeyboardInterrupt:
            break
    # print(idx)
    select_user_info = u_list[idx].split()
    print(f"\r恭喜中奖用户{select_user_info[0]} {select_user_info[1]}")
    return select_user_info[0]

def lottery_3(u_list):
    while 1:
        rand_x = random.randint(0,10000) / 10
        rand_y = random.randint(0,10000) / 10
        try:
            print(f'\r{rand_x},{rand_y}',end='')
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
    # print('')
    user_distance_list=[]
    for user_info in u_list:
        # print(user_info)
        uid, uname, ux, uy = user_info.split(' ')
        # 将字符串分离成列表
        distance = int((int(ux) - rand_x) ** 2 + (int(uy) - rand_y) ** 2)
        user_distance_list.append((uid, uname, distance))

        user_distance_list.sort(key=lambda x:x[2])
        # 对元素排序
    # print(f'\r{user_distance_list}')
    print(f"\r恭喜中奖用户{user_distance_list[0][0]} {user_distance_list[0][1]}")

def main():
    with open('user.txt',encoding='utf-8') as f:
        content = f.read()
        
    # print(content)
    user_list = content.split('\n')
    # print(user_list)

    lottery_1(user_list)
    lottery_2(user_list)
    lottery_3(user_list)

    
main()