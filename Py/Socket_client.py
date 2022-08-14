from fileinput import close
from pickletools import read_stringnl_noescape_pair
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import socket
import os
import pickle
import rsa
import hashlib



    
with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:

        s.connect(("127.0.0.1",1234))
        
      



        for i in range(1,5):
            message=input("请输入通信内容:")
            
            message = pad(str.encode(message), 16)
            # print(message)
            password = os.urandom(16)#AES密钥随机生成
            
            
            aes = AES.new(password,AES.MODE_ECB)  
            en_message = aes.encrypt(message)
            en_messageSha256=hashlib.sha256(en_message).hexdigest()
            # print(en_message)

        
            s.send(b"1")#1对应message
            time.sleep(0.5)
            s.send(b"0")
             
            
            time.sleep(0.5)
            s.send(pickle.dumps((en_message,en_messageSha256)))
            time.sleep(0.5)
            s.send(b"0")
            print("en_msg已发送") 

            # while True:
            #     data=s.recv(1024)
            #     if data:
            #         break
            #     else:
            #         print(data)
            time.sleep(0.5)
            s.send(b"3")#2对应pkey
            time.sleep(0.5)
            s.send(b"0")

            while True:
                data=s.recv(1024)
                if data==b"0":
                    serverpk=redata
                    
                    break
                else:
                    redata=data 
                         # print("data=",data)pl
                        
            pickserverpk,serverpkSha256=pickle.loads(serverpk)
            if hashlib.sha256(pickserverpk).hexdigest()==serverpkSha256:
                print("公钥已接收") 
                # print("serverpk=",serverpk)
                serverpk=pickle.loads(pickserverpk)
                en_password=rsa.encrypt(password,serverpk)
                print("密钥已加密")
                time.sleep(0.5)
                s.send(b"2")#2对应password
                time.sleep(0.5)
                s.send(b"0")

                time.sleep(0.5)
                s.send(en_password)
                time.sleep(0.5)
                s.send(b"0")
                print("密钥已传输")

                # while True:
                #     data=s.recv(1024)
                #     if data:
                #         break
                #     else:
                #         print(data)
                print("正在结束通信")
                time.sleep(0.5)
                s.send(b"-1")#2对应password
                time.sleep(0.5)
                s.send(b"0")
                print("已结束通信")

                # while True:
                #     data=s.recv(1024)
                #     if data:
                #         break
                #     else:
                #         print(data)  

            else:
                print("公钥已被篡改，已拒绝")
        



    


