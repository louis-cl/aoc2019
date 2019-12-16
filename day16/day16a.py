import sys
import math
from itertools import cycle, islice


pattern = [0,1,0,-1]

def repeat(p, k=1):
    for s in p:
        for i in range(k):
            yield s

def pattern_i(i):
    inf = cycle(pattern)
    repeated = repeat(inf, i+1)
    return islice(repeated, 1, None)


def fft(a):
    res = []
    for i in range(len(a)):
        sumi = 0
        for el,pi in zip(a, pattern_i(i)):
            sumi += el * pi
        res.append(abs(sumi) % 10)
    return res
        

def main(source):
    print(source)
    for _ in range(100):
        source = fft(source)
    print("RESULT", "".join(map(str, source[:8])))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].strip()
    # codes = "80871224585914546619083218645595"
    codes = [int(c) for c in codes]
    # read reactions
    main(codes)

