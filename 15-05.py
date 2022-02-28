
#!/usr/bin/env python3

import socket

host = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#s.bind((host, port))

print(s)

s.close()
