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
    if gdb_is:
        r = gdb.debug('./vuln','set debug-file-directory ./.debug/')
        # gdb.attach(r,'b* 0x4012ed')
        # gdb.attach(r)
        # pause()
        pass
    else:
        r = process("./vuln")
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0



def show_addr(name,addr):
      info(f'{name} = {hex(addr)}')

def revc_addr(r:process,name, until=b'\x7f',offset = 0)->int:
    if not offset:
        addr = u64(r.recvuntil(until).ljust(8,b'\x00'))
    else:
        addr = u64(r.recvuntil(until)[:offset].ljust(8,b'\x00'))
    show_addr(name,addr)
    return addr
    


elf = ELF(elf_path)
rop = ROP(elf)

r.interactive()