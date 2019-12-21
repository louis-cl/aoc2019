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

def main(mapa, begin, finish, warps, portalNames):
    queue = deque([(begin, 0, "AA,0")])
    depth = {(begin, 0): 0}
    while queue:
        pos, lvl, path = queue.popleft()
        dpos = depth[pos, lvl]
        for pos2 in (pos + d for d in dirs):
            if pos2 in mapa and mapa[pos2] == '.' and (pos2, lvl) not in depth:
                if pos2 == finish and lvl == 0:
                    print(path)
                    return dpos + 1
                depth[pos2, lvl] = dpos + 1
                queue.append((pos2, lvl, path))
        # warp
        if pos in warps:
            pos2, dlvl = warps[pos]
            if lvl == 0 and dlvl > 0: # can't use outer from lvl 0
                continue
            lvl2 = lvl + dlvl
            depth[pos2, lvl2] = dpos + 1
            path2 = path + f' / {portalNames[pos]},{lvl2}'
            queue.append((pos2, lvl2, path2))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip('\n'), lines))

    mapa = {}
    for i, line in enumerate(lines):
        # print(len(line))
        for j, c in enumerate(line):
            z = complex(i,j)
            if c == '#' or c == '.':
                mapa[z] = c

    # look for portals
    portals = {}
    h = len(lines)
    w = len(lines[0])
    # top
    for j,c in enumerate(lines[1]):
        if 'A' <= c <= 'Z':
            z = complex(2,j)
            portals[z] = lines[0][j] + c 
    # bottom
    for j,c in enumerate(lines[h-2]):
        if 'A' <= c <= 'Z':
            z = complex(h-3,j)
            portals[z] = c + lines[h-1][j]    
    # left
    for j in range(h):
        c = lines[j][0]
        if 'A' <= c <= 'Z':
            z = complex(j,2)
            portals[z] = c + lines[j][1]    
    # right
    for j in range(h):
        c = lines[j][-1]
        if 'A' <= c <= 'Z':
            z = complex(j,w-3)
            portals[z] = lines[j][-2] + c

    outPortals = portals
    portals = {}

    # inner portals
    i = 2
    j = 2
    while lines[i][j] != ' ':
        i += 1
        j += 1

    start = (i,j)
    while lines[i][j] != '#':
        j += 1
    j -= 1
    while lines[i][j] != '#':
        i += 1
    end = (i,j+1)
    print('start', start)
    print('end', end)
    
    # top
    for j in range(start[1], end[1]):
        c = lines[start[0]][j]
        if 'A' <= c <= 'Z':
            z = complex(start[0]-1, j)
            portals[z] = c + lines[start[0]+1][j]
    
    # left
    for i in range(start[0], end[0]):
        c = lines[i][start[1]]
        if 'A' <= c <= 'Z':
            z = complex(i, start[1]-1)
            portals[z] = c + lines[i][start[1]+1]
    # bottom
    for j in range(start[1], end[1]):
        c = lines[end[0]-1][j]
        if 'A' <= c <= 'Z':
            z = complex(end[0], j)
            portals[z] = lines[end[0]-2][j] + c
    # right
    for i in range(start[0], end[0]):
        c = lines[i][end[1]-1]
        if 'A' <= c <= 'Z':
            z = complex(i, end[1])
            portals[z] = lines[i][end[1]-2] + c

    inPortals = portals

    print("in", inPortals)
    print("out", outPortals)
    allPortals = {}
    allPortals.update(inPortals)
    allPortals.update(outPortals)

    warps = {}
    begin = None
    finish = None
    for p, name in allPortals.items():
        if name == 'AA':
            begin = p
        elif name == 'ZZ':
            finish = p
        else:
            other = next(p2 for p2, n2 in allPortals.items() if n2 == name and p2 != p)
            if p in inPortals:
                warps[p] = (other, -1)
            elif p in outPortals:
                warps[p] = (other, +1)
            else:
                raise Exception("bug")

    print("warps", warps)
    print("goals", begin, finish)
    draw(mapa)
    res = main(mapa, begin, finish, warps, allPortals)
    print("len", res)
