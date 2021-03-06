
#!/usr/bin/env python3

import socket

host = "127.0.0.1"
port = 12345

parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parent.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

parent.bind((host, port))

parent.listen(10)

(child, address) = parent.accept()

child.send("Thank you for connecting!".encode())

child.close()

parent.close()
