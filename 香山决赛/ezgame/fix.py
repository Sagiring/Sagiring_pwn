from AwdPwnPatcher import *
elf = AwdPwnPatcher('./pwn')
assembly = '''
mov rsi,rdi
xor rdi,rdi
mov rdx,1612
syscall
'''
elf.patch_by_jmp(0x4017FF, jmp_to=0x401809, assembly=assembly)
elf.save()