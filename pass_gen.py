
import random
import string
import argparse

def evaluate_password(password,show_info=True):
        result = False
        password_state = 0b00000

        for char in password:
            if char.isupper():
                password_state |=  0b10000
    
            elif char.islower():
                password_state |=  0b01000

            elif char.isdigit():
                password_state |=  0b00100
    
            else:
                password_state |=  0b00010
        if len(password) >= 8:
            password_state |=  0b00001
            

        if password_state == 0b11111:
            if show_info:
                print("Password is in rule")
            result=True
        else:
            if show_info:
                prompt="Password is not in rule,"
                if  password_state & 0b00001 == 0:
                    prompt+='len is not enough,'
                if  password_state & 0b10000 == 0:
                    prompt+='no upper char,'
                if  password_state & 0b01000 == 0:
                    prompt+='no lower char,'
                if  password_state & 0b00100 == 0:
                    prompt+='no digit,'
                if  password_state & 0b00010 == 0:
                    prompt+='no puctuation,'
                prompt=prompt[:-1]
                prompt+='.'
                print(prompt)

        return result

def generate_password():
    all_char_set = string.printable
    all_char_set*=9

    result=''.join(random.sample(all_char_set,k=9))
    return result

def creat_password(pass_length,confuse=False):
    result=''
    #TODO:生成包含各自字符
    result+=random.choice(string.ascii_uppercase)
    result+=random.choice(string.ascii_lowercase)
    result+=random.choice(string.digits)
    result+=random.choice(string.punctuation)
    if confuse:
        result+='Il'
        result+=''.join(random.sample(string.printable[:-6]*pass_length,pass_length-6))
    else:
        result+=''.join(random.sample(string.printable[:-6]*pass_length,pass_length-4))
    #TODO：生成指定长度的字符
    
    #TODO：随机打乱
    random.sample(result,len(result))
    return result

def main_userinput():
    while 1:
        # 用户输入密码
        user_password = input("请输入:")
        # 判断合理性
        if evaluate_password(user_password):
            break



def main_genpassword():
    while 1:
        user_password = generate_password()
        if evaluate_password(user_password,show_info=False):
            print(f'新生成密码为:{user_password}')
            break

def main():
    # 命令符调用的说明与配置
    parser = argparse.ArgumentParser(description='Generate new password.')
    parser.add_argument('-l','--length',type=int, default=9,
                        help='an integer for the length of password')
    parser.add_argument('-c','--confuse',action='store_true',
                        help='use confuse characters (I & l)')
    args = parser.parse_args()

    # print(f'confuse:{args.confuse}')
    # print(args.length)
    print(f'新生成密码为:{creat_password(args.length,args.confuse)}')
main()