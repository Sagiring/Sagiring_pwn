import app
import os
import random
import string


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def create_random_folder():
    folder_name = "./tmp/" +generate_random_string(7)
    while True:
        if os.path.exists(folder_name):
            folder_name = generate_random_string(16)
        else:
            os.mkdir(folder_name)
            return folder_name

folder_name =  create_random_folder()



while True:
    choice = input("> ")
    if choice == '0':
        app.app_main(folder_name)
        pass
    elif choice == '1':
        app.calc(folder_name)
    elif choice == '2':
        app.load_arr(folder_name)
    else:
        print("Bye~")
        break
