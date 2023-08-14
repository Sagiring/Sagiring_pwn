from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./shaokao")
    
else:
    host = "192.168.0.111:19787"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # gdb.attach(r,'b* 0x00401571')
    gdb.attach(r)
    pause()
    pass
right = b'BlackBird'
wrong = b'WingS'

for i in range(100):
    context = r.recvuntil(b'=')
    result = r.recv()
    a = context.decode().split('\n')[-1].split('+')[0]
    b = context.decode().split('\n')[-1].split('+')[1]
    if int(a)+int(b[:-1]) == int(result):
        r.sendline(right)
        print(right)
    else:
        r.sendline(wrong)
        print(wrong)
   

r.interactive()
