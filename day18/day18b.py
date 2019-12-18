import sys
from collections import deque
import heapq
import math
sys.path.append('..')
from utils import draw

dirs = [
    complex(0,1),
    complex(1,0),
    complex(-1,0),
    complex(0,-1)
]

def objectives(mapa, start, keys):
    found = {}
    depth = {start: 0}
    queue = deque([start])

    while queue:
        pos = queue.popleft()
        d_i = depth[pos]
        for p_new in (pos + d for d in dirs):
            tile = mapa[p_new]
            if tile == '#' or p_new in depth:
                continue
            depth[p_new] = d_i+1
            if tile >= 'A' and tile <= 'Z':
                if tile.lower() in keys:
                    queue.append(p_new)                    
            elif tile >= 'a' and tile <= 'z':
                if tile not in keys:
                    found[p_new] = (tile, d_i+1)
                else:
                    queue.append(p_new)
            elif tile == '.' or tile == '@':
                queue.append(p_new)
            else:
                raise Exception("INVALID tile")
    return found


def update_tuple(old, i, value):
    s = list(old)
    s[i] = value
    return tuple(s)

def update_keys(old, key):
    return ''.join(sorted(old+key))

class Entry:
    def __init__(self, a, b, c):
        self.value = (a,b,c)
    def __lt__(self, obj):
        return self.value[:2] < obj.value[:2]
    def __repr__(self):
        return str(self.value)
    def __str__(self):
        return str(self.value)

def main(mapa, starts, n):
    starts = tuple(starts)
    depth = {}
    queue = []
    heapq.heappush(queue, Entry(0,"",starts))
    depth["", starts] = 0 

    while queue:
        # print("\nQUEUE", queue)
        entry = heapq.heappop(queue)
        if len(depth) % 100: # doing shit
            print(entry)
        cost, keys, poss = entry.value
        cost = depth[keys, poss]
        if len(keys) == n:
            print("found", entry)
            return
        # d_i = depth[poss, keys]
        # print('from', entry)
        for i, pos in enumerate(poss):
            targets = objectives(mapa, pos, keys)
            # print(i, 'targets', targets)
            for p, (key, dist) in targets.items():
                costi = cost+dist
                keysi = update_keys(keys, key)
                possi = update_tuple(poss, i, p)
                if (keysi, possi) in depth and depth[keysi, possi] <= costi:
                    continue
                # print('adding', costi, keysi, possi)
                depth[keysi, possi] = costi
                heapq.heappush(queue, Entry(costi, keysi, possi))


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

    # change map around @
    starts = []
    for i in range(-1,2):
        for j in range(-1,2):
            z = start + complex(i,j)
            if i == 0 or j == 0:
                mapa[z] = '#'
            else:
                mapa[z] = '@'
                starts.append(z)

    print("starts", starts)
    draw(mapa)

    main(mapa, starts, len(keys))
    


