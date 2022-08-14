import string
while 1:
    user_password= input("请输入:")

    # 判断合理性
    
    

    have_upper = False
    have_lower = False
    have_digit = False
    have_puctuation = False
    have_len= len(user_password) >= 8

    for char in user_password:
        if char in string.ascii_uppercase:
            have_upper = True
        elif char in string.ascii_lowercase:
            have_lower = True
        elif char in string.digits:
            have_digit = True
        else:
            have_puctuation = True

    # 输出
    is_secure = (have_upper
                and have_len 
                and have_lower 
                and have_digit 
                and have_puctuation)
    
    if is_secure:
        print("Password is in rule")
        break
    else:
        prompt="Password is not in rule,"
        if not have_len:
            prompt+='len is not enough,'
        if not have_upper:
            prompt+='no upper char,'
        if not have_lower:
            prompt+='no lower char,'
        if not have_digit:
            prompt+='no digit,'
        if not have_puctuation:
            prompt+='no puctuation,'
        prompt=prompt[:-1]
        prompt+='.'
        print(prompt)
