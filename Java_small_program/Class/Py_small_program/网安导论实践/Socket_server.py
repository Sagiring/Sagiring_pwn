# from curses import keyname
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import time
import socket
import rsa
import pickle
import hashlib
import threading


(pkey, key) = rsa.newkeys(512)

def handle_client(c,addr):
    with c:

            print(addr,"connected.")
           

            
            for i in range(1,5):
                
                issocket=b"0"
                password=''
                en_message=''
                den_message=''
                en_password=''

                while issocket==b"1" or issocket==b"2" or issocket==b"0" or issocket==b"3":

                    while True:
                        data=c.recv(1024)
                        if data==b"0":
                            issocket=redata
                            break
                        else:
                            redata=data 
                            # print("data=",data)pl
                            
                        

                    # print("issocket=",issocket)

                    if issocket==b"1":
                        while True:
                            data=c.recv(1024)
                            if data==b"0":
                                en_picklemessage=redata
                                break
                            else:
                                redata=data 
                                # print("data=",data)
                        en_message,en_messageSha256 = pickle.loads(en_picklemessage)
                        if hashlib.sha256(en_message).hexdigest()==en_messageSha256:

                            print("已接收密文：",en_message)
                            # c.send("message Recieved".encode("utf-8"))
                        else:
                            print("密文已被篡改 已拒绝")
                            break

                    if issocket==b"2":
                        while True:
                            data=c.recv(1024)
                            if data==b"0":
                                en_password=redata
                                break
                            else:
                                redata=data 
                                # print("data=",data) 
                        print("正在解密密钥")

                        password = rsa.decrypt(en_password, key)
                           
                        print("RSA解密成功,密钥已解出") 
                        # c.sendall("password Recieved".encode("utf-8"))
                    if issocket==b"3":
                        PickPkey=pickle.dumps(pkey)#用pickle进行序列化来进行hash
                        PkeySha256 = hashlib.sha256(PickPkey).hexdigest()
                        c.send(pickle.dumps((PickPkey,PkeySha256)))

                        time.sleep(0.5)
                        c.send(b"0")
                        time.sleep(0.5)
                        print("已发送公钥")
                    
                    if issocket==b"-1":
                        print("通信结束正在解密明文")
                        aes = AES.new(password,AES.MODE_ECB)
                        den_message = aes.decrypt(en_message)
                        den_message=unpad(den_message,16)
                        print("明文：",den_message.decode("utf-8"))  
                        # c.sendall("Socket close".encode("utf-8"))
                        
                        break


with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
        s.bind(("0.0.0.0",1234))
        s.listen()

        for i in range(1,5):
            c, addr=s.accept()

            t=threading.Thread(target=handle_client,args=(c,addr))
            t.start()
        
                
            
  