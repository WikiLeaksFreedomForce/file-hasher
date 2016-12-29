import glob
from timeit import default_timer as timer
from binascii import unhexlify
import json

with open('ripemd160.json', 'rb') as f:
    hashes = json.loads(f.read())


def check_hash(hexcode):
    '''
    This will return whether or not a wikileaks file hash is inside the blockchain
    '''
    return ' '.join('{}'.format(key)
                    for key, values in hashes.iteritems()
                    if unhexlify(values) in hexcode)


totalstart = timer()
for files in glob.glob("*.dat"):
    start = timer()
    file = open(files, "r")
    hashfound = check_hash(file.read())
    if hashfound != '':
        print(hashfound, files)

    print("Filename: {0} | time: {1:.2f}s"
          .format(files, timer() - start))

print(timer() - totalstart)
