from pwn import * 
from pwn import p64
import socket

context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']
# ip = "121.4.111.50"
# r = remote(ip,30526)#远程连接
r = process("./pwn")
r.sendlineafter(b"Enter your flag:\n",p64("0"))

r.recvall()

