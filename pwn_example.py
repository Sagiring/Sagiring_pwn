from pwn import * 
from pwn import p64
import socket
from ctypes import *

debug = 0
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect('43.241.16.222',30709)#远程连接
    gdb_is =0
# elf = cdll.LoadLibrary('libc.so.6')
# elf = ELF('./pwn')

if gdb_is:
    gdb.attach(r,'*b 0x4012ed')
    pause()
    pass

# r.sendlineafter()
# r.send()
# r.recvuntil()
r.interactive()
