import re
import sys
import glob
from timeit import default_timer as timer

totalstart = timer()
for files in glob.glob("*.dat"):
    start = timer()
    file = open(files, "r")
    if re.search(sys.argv[1], file.read()):
        print("Filename: {0} |  found {1}"
              .format(files, sys.argv[1]))

    print("Filename: {0} | time: {1:.2f}s"
          .format(files, timer() - start))
print(timer()-totalstart)
