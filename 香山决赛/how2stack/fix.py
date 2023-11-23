from AwdPwnPatcher import *
elf = AwdPwnPatcher('./pwn')

assembly = '''
mov eax,0x62
'''
elf.patch_origin(0x01765,0x00000176B,assembly=assembly)
elf.save()
