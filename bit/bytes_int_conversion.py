"""
In memory, bytes (8 bits) are stored either big or little endian memory address
depending on the CPU.

Issues occur when computer is storing bytes of data as multi-bytes such as
storing floats, long or ASCII.

Big endian stores the first byte as the largest in memory address.
Little endian stores the first byte as the smallest in memory address.

eg

To store the number 258 requires two memory addresses because a memory address
can only store from 0 to 255.

The first and second address will be 0x01 and 0x02, respectively.
Big endian will store the most significant byte first, thus 258 is stored
as 0x0102.
Little endian will store the first byte as last, hence 258 is stored as
0x0201.

"""
from collections import deque


def int_to_bytes_big_endian(num):
    bytestr = deque()
    while num > 0:
        # list.insert(0, ...) is inefficient
        bytestr.appendleft(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def int_to_bytes_little_endian(num):
    bytestr = []
    while num > 0:
        bytestr.append(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def bytes_big_endian_to_int(bytestr):
    num = 0
    for b in bytestr:
        num <<= 8
        num += b
    return num


def bytes_little_endian_to_int(bytestr):
    num = 0
    e = 0
    for b in bytestr:
        num += b << e
        e += 8
    return num
