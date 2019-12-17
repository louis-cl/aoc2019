import sys
from collections import deque
import math
sys.path.append('..')
from day9.day9b import program

def draw(tiles):
    max_y = int(max(z.imag for z in tiles.keys()))
    max_x = int(max(z.real for z in tiles.keys()))

    for i in range(max_x+1):
        for j in range(max_y+1):
            if complex(i,j) in tiles:
                print(tiles[complex(i,j)], end='')
            else:
                print(' ', end='')
        print()


def scaffold(mapa, start, diri):
    print(start, diri)
    seen = set()

    total = 0
    p = start
    while True:
        # try to go forward
        seen.add(p)
        next_p = p + diri
        # print("from", p, next_p)
        if next_p not in mapa:
            # print("not in")
            # need to turn
            ccw = diri * 1j
            if p+ccw in mapa:
                diri = ccw
                p += ccw
            elif p-ccw in mapa:
                diri = -ccw
                p += -ccw
            else:
                break
        elif next_p in seen:
            # print('already seen')
            mapa[next_p] = 'O'
            total += next_p.imag * next_p.real
            p = next_p + diri
        else:
            p = next_p
        # print('final', p, diri)
    print(total)

def main(codes):
    memory = {i:v for i,v in enumerate(codes)}
    read = deque()
    p = program(memory, read)


    mapa = {}

    i = 0
    j = 0
    start = None
    diri = None
    try:
        while True:
            r = next(p)
            if r == 10:
                print()
                i += 1
                j = 0
            else:
                c = chr(r)
                if c == '#':
                    mapa[complex(i,j)] = c
                elif c == '^':
                    start = complex(i,j)
                    diri = complex(-1, 0)
                j += 1
                print(c, end='')
    except StopIteration:
        pass
    
    scaffold(mapa, start, complex(0,-1))
    draw(mapa)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    # read reactions
    main(codes)

    

