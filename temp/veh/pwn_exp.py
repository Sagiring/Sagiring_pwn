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
        r = process("./pwn")
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug("./pwn")
    # pause()
    pass

# r.interactive()
def add(size):
    r.sendafter(b'choice:\n',b'1')
    r.sendafter(b'input size:\n',size.encode())

def free():
    r.sendafter(b'choice:\n',b'3')

def edit(contents):
    r.sendafter(b'choice:\n',b'2')
    r.sendafter(b'contents:\n',contents.encode())

add(0x80)
add(0x80)
pause()
r.interactive()