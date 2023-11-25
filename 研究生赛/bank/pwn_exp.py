
from pwn import *
from pwn import p32

e = ELF('./pwn')

e.write(0x4020E9+1, p32(0x20))

e.save('./pwn.p')