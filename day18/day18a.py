import sys
from collections import deque
import math
sys.path.append('..')
# from utils import draw

dirs = [
    complex(0,1),
    complex(1,0),
    complex(-1,0),
    complex(0,-1)
]

def main(mapa, start, n):
    depth = {}
    depth[(start, "")] = 0
    queue = deque([(start, "")])

    while queue:
        # print("STEP", queue)
        entry = queue.popleft()
        d_i = depth[entry]
        pos, keys = entry
        for p_new in (pos + d for d in dirs):
            tile = mapa[p_new]
            if tile == '#':
                continue
            elif tile >= 'A' and tile <= 'Z':
                if tile.lower() in keys:
                    entry2 = (p_new, keys)
                    if entry2 not in depth:
                        queue.append(entry2)
                        depth[entry2] = d_i+1
            elif tile >= 'a' and tile <= 'z':
                if tile not in keys:
                    entry2 = (p_new, ''.join(sorted(keys+tile)))
                    if len(entry2[1]) == n:
                        print("FOUND ALL KEYS", d_i+1)
                        return d_i+1
                else:
                    entry2 = (p_new, keys)
                if entry2 not in depth:
                    queue.append(entry2)
                    depth[entry2] = d_i+1
            elif tile == '.' or tile == '@':
                entry2 = (p_new, keys)
                if entry2 not in depth:
                    queue.append(entry2)
                    depth[entry2] = d_i+1
            else:
                raise Exception("INVALID tile")




if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip(), lines))
    h = len(lines)
    w = len(lines[0])

    mapa = {}
    start = None
    keys = set()
    for i in range(h):
        for j in range(w):
            z = complex(i,j)
            c = lines[i][j]
            mapa[z] = c
            if c == '@':
                start = z
            elif c <= 'z' and c >= 'a':
                keys.add(c)

    print("start", start)
    print("need", len(keys))
    # draw(mapa)
    main(mapa, start, len(keys))
    


