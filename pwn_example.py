from pwn import * 
from pwn import p64
import socket
from ctypes import *

# context(arch='i386',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
host = "week-1.hgame.lwsec.cn"
ip = socket.gethostbyname(host)
r = remote(ip,31158)#远程连接

# elf = cdll.LoadLibrary('libc.so.6')
# elf = ELF('./pwn')

# r = process("./pwn")
# gdb.attach(r)
# pause()
# r.sendlineafter()
r.interactive()
