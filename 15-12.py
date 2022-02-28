
#!/usr/bin/env python3

import hashlib

md5 = hashlib.md5("1234".encode()).hexdigest()
print(md5)

sha256 = hashlib.sha256("1234".encode()).hexdigest()
print(sha256)

sha512 = hashlib.sha512("1234".encode()).hexdigest()
print(sha512)
