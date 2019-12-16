import sys
import math
from itertools import accumulate

def toInt(digits):
    return int("".join(map(str, digits)))

def main(source):
    offset = toInt(source[:7])
    print("offset", offset)
    
    arr = source * 10000
    n = len(arr)
    arri = arr[n-1:offset-1:-1]
    for _ in range(100):
        arri = list(accumulate(arri, lambda a,b: abs(a+b)%10))
    
    print("RES", toInt(arri[:-9:-1]))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].strip()
    codes = [int(c) for c in codes]
    # read reactions
    main(codes)

