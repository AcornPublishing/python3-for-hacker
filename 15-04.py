
#!/usr/bin/env python3

import socket

host = "localhost"

port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))

print(s)

s.close()
