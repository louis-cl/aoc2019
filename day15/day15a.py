import sys
from collections import deque
import math
sys.path.append('..')
from day9.day9b import program

def draw(mapa):
    print("\nDRAWING")
    max_y = max(int(k.imag) for k in mapa.keys())
    max_x = max(int(k.real) for k in mapa.keys())

    min_y = min(int(k.imag) for k in mapa.keys())
    min_x = min(int(k.real) for k in mapa.keys())

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            p = complex(i,j)
            if p in mapa:
                print(mapa[p], end='')
            else:
                print(' ', end='')
        print()

dirs = {
    1: complex(0,1),
    2: complex(0,-1),
    3: complex(-1,0),
    4: complex(1,0)
}

reverse = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

def explore(pos, p, read, mapa):
    for k,d in dirs.items():
        # try going in dir d
        newPos = pos + d
        if newPos in mapa:
            continue
        read.append(k)
        result = next(p)
        if result == 0:
            mapa[newPos] = '#'
        elif result == 1:
            mapa[newPos] = '.'
            explore(newPos, p, read, mapa)
            # undo
            read.append(reverse[k])
            next(p)
        elif result == 2:
            mapa[newPos] = '$'
            read.append(reverse[k])
            next(p)


def shortest(pos, mapa):
    queue = deque([pos])
    depth = {pos: 0}
    while queue:
        p_i = queue.popleft()
        d_i = depth[p_i]
        for p_new in (p_i + d for d in dirs.values()):
            tile = mapa[p_new]
            if tile == '$':
                return d_i+1
            elif tile == '#':
                continue
            if p_new not in depth:
                depth[p_new] = d_i+1
                queue.append(p_new)


def main(codes):
    memory = {i:v for i,v in enumerate(codes)}
    read = deque()
    p = program(memory, read)

    mapa = {}
    pos = complex(0,0)
    mapa[pos] = 'S'
    explore(pos, p, read, mapa)
    draw(mapa)
    print("steps", shortest(pos, mapa))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    # read reactions
    main(codes)

