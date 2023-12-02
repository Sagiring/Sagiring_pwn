from pwn import * 
from pwn import p64,u64
from LibcSearcher import *
from pwnUtils import *


debug = 1
gdb_is = 0
attach_is = 0
elf_path = "./pwn"
host = "192.168.0.111:53783"
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        if attach_is:
            r = process(elf_path) 
            gdb.attach(r)
            # gdb.attach(r,'b* 0x4012ed')
            pause()
        else:
            r = gdb.debug(elf_path,'set debug-file-directory ./.debug/')
    else:
        r = process(elf_path) 
else:
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0


elf = ELF(elf_path)
# libc = ELF()
rop = ROP(elf)


r.interactive()