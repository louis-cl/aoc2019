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

# def objectives(mapa, start, keys):
#     found = {}
#     depth = {start: 0}
#     queue = deque([start])

#     while queue:
#         pos = queue.popleft()
#         d_i = depth[pos]
#         for p_new in (pos + d for d in dirs):
#             tile = mapa[p_new]
#             if tile == '#' or p_new in depth:
#                 continue
#             depth[p_new] = d_i+1
#             if tile >= 'A' and tile <= 'Z':
#                 if tile.lower() in keys:
#                     queue.append(p_new)                    
#             elif tile >= 'a' and tile <= 'z':
#                 if tile not in keys:
#                     found[p_new] = (tile, d_i+1)
#                 else:
#                     queue.append(p_new)
#             elif tile == '.' or tile == '@':
#                 queue.append(p_new)
#             else:
#                 raise Exception("INVALID tile")
#     return found

def main(mapa, begin, finish, warps):
    queue = deque([begin])
    depth = {begin: 0}
    while queue:
        pos = queue.popleft()
        dpos = depth[pos]
        for pos2 in (pos + d for d in dirs):
            if pos2 in mapa and mapa[pos2] == '.' and pos2 not in depth:
                if pos2 == finish:
                    return dpos + 1
                depth[pos2] = dpos + 1
                queue.append(pos2)
        # warp
        if pos in warps:
            pos2 = warps[pos]
            depth[pos2] = dpos + 1
            queue.append(pos2)


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
    print("portals", portals)
    
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

    
    warps = {}
    begin = None
    finish = None
    for p, name in portals.items():
        if name == 'AA':
            begin = p
        elif name == 'ZZ':
            finish = p
        else:
            other = next(p2 for p2, n2 in portals.items() if n2 == name and p2 != p)
            warps[p] = other

    print("warps", warps)
    print("goals", begin, finish)
    draw(mapa)

    res = main(mapa, begin, finish, warps)
    print("res", res)
