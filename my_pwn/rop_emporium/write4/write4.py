from pwn import * 
from pwn import p64
import socket
from ctypes import *
context(arch='amd64',os = 'linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libwrite432.so')
r = process("./write4")

payload = 0

pause()

r.sendlineafter(b">", payload)

r.interactive()
