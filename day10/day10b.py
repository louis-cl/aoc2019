import sys
import math
from itertools import groupby
from more_itertools import roundrobin

def sign(x):
    if x == 0: return 0
    return 1 if x > 0 else -1

def toDir(z):
    dx,dy = z
    if dx == 0 or dy == 0:
        d = (sign(dx),sign(dy))
    else:
        gcd = math.gcd(dx,dy)
        d = (dx//gcd, dy//gcd)
    return d

def covering(pos, mapa):
    # return how many asteroids i'm covering
    usedDir = set()
    (a,b) = pos
    for (x,y) in mapa:
        dx, dy = (x-a, y-b)
        usedDir.add(toDir((dx,dy)))
    return len(usedDir)

def dist2(a,b):
    x1,y1 = a
    x2,y2 = b
    return (x1-x2)**2 + (y1-y2)**2

def angleUp(a):
    x,y = a
    # reverse y to orient basis positively (y up, x right)
    ang = -math.atan2(-y, x) + math.atan2(1,0)
    if ang < 0: ang += 2*math.pi
    return ang

def main(mapa):
    # part1
    max_covering = 0
    start, max_covering = max(((p,covering(p, mapa)) for p in mapa), key=lambda x:x[1])
    print("covering", max_covering-1, "from", start)

    # part2
    mapa.remove(start)    
    angleOrder = lambda x: angleUp(toDir((x[0]-start[0], x[1]-start[1])))
    res = sorted(mapa, key=angleOrder)
    res = (sorted(g, key=lambda x: dist2(x, start)) for _,g in groupby(res, key=angleOrder))
    res = list(roundrobin(*res))
    print(res)

    print("200th ",res[199])

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    mapa = set()
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c == '#':
                mapa.add((j,i))
    main(mapa)