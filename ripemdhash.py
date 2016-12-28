import hashlib as h
import sys

sha256sum = h.sha256()
ripe = h.new('ripemd160')

with open(sys.argv[1], 'rb') as filehash:
    while True:
        buf = filehash.read(65536)
        if not buf:
            break
        sha256sum.update(buf)

print(h.new('ripemd160', sha256sum.digest()).hexdigest())
