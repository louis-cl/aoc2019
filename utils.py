from math import gcd 
from functools import reduce
import re

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def integers(s):
    return re.findall(r'-?\d+', s.strip())

# tiles is a dict complex -> char
# top left is (0,0) -> (x,y)
def draw(tiles, tileset=None):
    max_y = int(max(z.imag for z in tiles.keys()))
    max_x = int(max(z.real for z in tiles.keys()))

    def tile(t):
        return tileset.get(t, t) if tileset else t

    for i in range(max_x+1):
        for j in range(max_y+1):
            z = complex(i,j)
            if z in tiles:
                print(tile(tiles[z]), end='')
            else:
                print(' ', end='')
        print()