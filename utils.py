from math import gcd 
from functools import reduce
import re

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def integers(s):
    return re.findall(r'-?\d+', s.strip())

# tiles is a dict complex -> char
# top left is (0,0) -> x is row, y is column
# screen means         x is column, y is row
def draw(tiles, tileset=None, screen=False):
    max_y = int(max(z.imag for z in tiles.keys()))
    max_x = int(max(z.real for z in tiles.keys()))

    def tile(t):
        return tileset.get(t, t) if tileset else t
        
    if screen:
        for y in range(max_y+1):
            for x in range(max_x+1):
                z = complex(x,y)
                if z in tiles:
                    print(tile(tiles[z]), end='')
                else:
                    print(' ', end='')
            print()
    else:
        for x in range(max_x+1):
            for y in range(max_y+1):
                z = complex(x,y)
                if z in tiles:
                    print(tile(tiles[z]), end='')
                else:
                    print(' ', end='')
            print()