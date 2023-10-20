from pwn import * 
from pwn import p64
import socket
from ctypes import *
context(arch='amd64',os = 'linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
elf = cdll.LoadLibrary("./libc-2.23.so")
r = process("./hello")



r.interactive()
