import string
while 1:
    user_password= input("请输入:")

    # 判断合理性
    
    
    password_state=0b00000
    # have_upper = False
    # have_lower = False
    # have_digit = False
    # have_puctuation = False
    

    for char in user_password:
        if char in string.ascii_uppercase:
            password_state |=  0b10000
             # have_upper = True
        elif char in string.ascii_lowercase:
            password_state |=  0b01000
            # have_lower = True
        elif char in string.digits:
            password_state |=  0b00100
            # have_digit = True
        else:
            password_state |=  0b00010
            # have_puctuation = True

    if len(user_password) >= 8:
        password_state |=  0b00001
        

    # 输出
    # is_secure = (have_upper
    #             and have_len 
    #             and have_lower 
    #             and have_digit 
    #             and have_puctuation)
    # is_secure = (password_state == 0b11111) 
    
    if password_state == 0b11111:
        print("Password is in rule")
        break
    else:
        prompt="Password is not in rule,"
        if  password_state & 0b00001 == 0b00001:
            prompt+='len is not enough,'
        if  password_state & 0b10000 == 0b10000:
            prompt+='no upper char,'
        if  password_state & 0b01000 == 0b01000:
            prompt+='no lower char,'
        if  password_state & 0b00100 == 0b00100:
            prompt+='no digit,'
        if  password_state & 0b00010 == 0b00010:
            prompt+='no puctuation,'
        prompt=prompt[:-1]
        prompt+='.'
        print(prompt)
#123