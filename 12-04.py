
#!/usr/bin/env python3

import struct

print(struct.pack("i", 2))
print(struct.pack("ii", 1, 2))
print(struct.pack("il", 1, 2))
print(struct.pack("<il", 1, 2))
print(struct.pack(">il", 1, 2))
print(struct.pack("!il", 1, 2))

pack = struct.pack("il", 1, 2)
print(pack)
unpack = struct.unpack("il", pack)
print(unpack)
