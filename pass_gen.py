import string

def evaluate_password(password):
        result=False
        password_state=0b00000

        for char in password:
            if char in string.ascii_uppercase:
                password_state |=  0b10000
    
            elif char in string.ascii_lowercase:
                password_state |=  0b01000

            elif char in string.digits:
                password_state |=  0b00100
    
            else:
                password_state |=  0b00010
        if len(password) >= 8:
            password_state |=  0b00001
            

        if password_state == 0b11111:
            print("Password is in rule")
            result=True
        else:
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


def main():
    while 1:
        # 用户输入密码
        user_password= input("请输入:")
        # 判断合理性
        if evaluate_password(user_password):
            break

main()





