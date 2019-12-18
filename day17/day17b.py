import sys
from collections import deque
import math
sys.path.append('..')
from day9.day9b import program
from day17.compress import regexp
from utils import draw

def computePath(mapa, start, diri):
    # hardcoded starting conditions
    path = ['L'] 
    diri = complex(0,-1)

    forwardCount = 0
    p = start
    while True:
        # try to go forward
        next_p = p + diri
        # print("from", p, next_p)
        if next_p not in mapa:
            # print("not in")
            # need to turn
            ccw = diri * 1j
            if p+ccw in mapa:
                diri = ccw
                p += ccw
                path.append(forwardCount)
                forwardCount = 1
                path.append('L')
            elif p-ccw in mapa:
                diri = -ccw
                p += -ccw
                path.append(forwardCount)
                forwardCount = 1
                path.append('R')
            else:
                break
        else:
            p = next_p
            forwardCount += 1
        # print('final', p, diri)
    if forwardCount > 0:
        path.append(forwardCount)
    return path

def main(codes):
    memory = {i:v for i,v in enumerate(codes)}
    read = deque()
    p = program(memory.copy(), read)

    mapa = {}

    i = 0
    j = 0
    start = None
    diri = None
    try:
        while True:
            r = next(p)
            if r == 10:
                i += 1
                j = 0
            else:
                c = chr(r)
                if c == '#':
                    mapa[complex(i,j)] = c
                elif c == '^':
                    mapa[complex(i,j)] = '^'
                    start = complex(i,j)
                    diri = complex(-1, 0)
                j += 1
                # print(c, end='')
    except StopIteration:
        pass

    path = computePath(mapa, start, diri)
    # scaffold(mapa, start, complex(0,-1))
    draw(mapa)

    pathStr =",".join(map(str, path)) + ","
    

    # send main routine
    routine, methods = regexp(pathStr)

    # A = ['L', 10, 'L', 8, 'R', 12]
    # B = ['L', 8, 'L', 10, 'L', 6, 'L', 6]
    # C = ['L', 6, 'R', 8, 'R', 12, 'L', 6, 'L', 8]
    # routine = ['C','A','C','B','A','B','A','C','B','A']

    inp = ",".join(routine) + '\n'
    for m in methods:
        inp += m[:-1] + "\n"
    inp += "n\n"

    mem2 = memory.copy()
    mem2[0] = 2
    read2 = deque(map(ord, inp))
    p = program(mem2, read2)
    # while True:
        # res = next(p)
        # print('>', res, chr(res)))
    *_, res = p
    print(">", res)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    # read reactions
    main(codes)

    


