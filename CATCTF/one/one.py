from pwn import * 
from pwn import p64
import socket
from ctypes import *
context(arch='amd64',os = 'linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('libc.so.6')
r = process("./pwn")
# elf = ELF('./pwn')

# pause()

r.sendlineafter(b"USER NAME:",b"HRPHRP")
r.sendlineafter(b"PASSWORD:",b"PWNME")

r.interactive()
