
#!/usr/bin/env python3

import socket, struct

k = struct.unpack("i", socket.inet_aton("127.0.0.1"))
print(k)

k = socket.inet_ntoa(struct.pack("i", 16777343))
print(k)

x = 0x00FF
print(int(x))

x = socket.htons(x)
print(x)

x = socket.ntohs(x)
print(x)
