from pwn import * 
from pwn import p64,u64

elf = ELF('./vuln')
libc = ELF('./libc-2.32.so')
rop = ROP(elf)



info(rop.search())