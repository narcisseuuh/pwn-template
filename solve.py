from pwn import *
from os import environ

exe = ELF(b'./binary')
libc = ELF(b'./libc.so.6')

gdbscript = """
break main 
c
"""

def conn():
    if environ['DBG'] == 'YES':
        return gdb.debug([exe.path], gdbscript = gdbscript)
    elif environ['LOCAL'] == 'YES':
        return process([exe.path])
    else:
        return remote('ip', porto)





def main():
    r = conn()


    r.interactive()


if __name__ == '__main__':
    main()
