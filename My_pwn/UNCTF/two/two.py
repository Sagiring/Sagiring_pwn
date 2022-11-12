from pwn import * 
from pwn import p64
import socket

context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,34405)#远程连接

r = process("./pwn")
r.sendlineafter('input a num:',b'100')
if(r.recv() == b"Success!!!"):
    print("1")

   

