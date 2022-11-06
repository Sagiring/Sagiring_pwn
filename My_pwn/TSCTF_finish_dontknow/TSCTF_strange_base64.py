from pwn import * 
from pwn import p64
import re
import base64
ip = '121.4.73.103'
r = remote(ip,10007)#远程连接
while 1:
    response = r.recv().decode()
    if 'b' not in response:
        print(response)
        break
    else:
        i = re.search("b'(.*)'",response).group(0)[2:-1]
        r.sendline(base64.b64decode(i).decode())
        print(response)
r.recvall()


