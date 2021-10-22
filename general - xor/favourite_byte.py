decode_msg = bytearray.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

flag = ""

for b in decode_msg:
    flag += chr(b ^ 16)

print(flag)
