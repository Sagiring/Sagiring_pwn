import random
import string


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


def main_userinput():
    while 1:
        # 用户输入密码
        user_password = input("请输入:")
        # 判断合理性
        if evaluate_password(user_password):
            break


def generate_password():
    all_char_set = string.ascii_lowercase \
    +string.ascii_uppercase \
    +string.digits \
    +string.punctuation
    all_char_set*=9

    result=''.join(random.sample(all_char_set,k=9))
    return result


def main():
    while 1:
        user_password = generate_password()
        if evaluate_password(user_password,show_info=False):
            print(f'新生成密码为:{user_password}')
            break



main()