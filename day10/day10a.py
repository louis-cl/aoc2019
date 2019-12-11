import sys
import math

def sign(x):
    if x == 0: return 0
    return 1 if x > 0 else -1


def covering(pos, mapa):
    # return how many asteroids i'm covering
    usedDir = set()
    (a,b) = pos
    for (x,y) in mapa:
        dx, dy = (x-a, y-b)
        if dx == 0 or dy == 0:
            d = (sign(dx),sign(dy))
        else:
            gcd = math.gcd(dx,dy)
            d = (dx//gcd, dy//gcd)
        usedDir.add(d)
    return len(usedDir)


def main(mapa):
    max_covering = max(covering(p, mapa) for p in mapa)
    print("covering", max_covering-1)  


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # lines[0] = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    mapa = set()
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c == '#':
                mapa.add((j,i))
    main(mapa)