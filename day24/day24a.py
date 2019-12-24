import sys
from collections import deque, defaultdict
import heapq
import math
sys.path.append('..')
import re
import random
from utils import draw

dirs = [
    complex(1,0),
    complex(0,1),
    complex(-1,0),
    complex(0,-1)
]

def n_adj(mapa, p):
    return sum(z in mapa and mapa[z] == '#' for z in (p + d for d in dirs))

def step(mapa):
    map2 = {}
    for k in mapa:
        n = n_adj(mapa, k)
        if mapa[k] == '#':
            map2[k] = '#' if n == 1 else '.'
        else:
            map2[k] = '#' if n in [1,2] else '.'
    return map2

def serialize(mapa):
    elements = []
    for i in range(5):
        # if i > 0: elements.append('\n')
        for j in range(5):
            z = complex(i,j)
            elements.append(mapa[z])
    return ''.join(elements)

def biodiversity(s):
    div = 0
    for i,c in enumerate(s):
        if c == '#':
            div += pow(2,i)
    return div

def main(mapa):
    seen = set([serialize(mapa)])
    while True:
        mapa = step(mapa)
        s = serialize(mapa)
        if s in seen:
            print("FOUND repeated", s, biodiversity(s))
            break
        seen.add(s)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip('\n'), lines))
    mapa = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                mapa[complex(i,j)] = '#'
            else:
                mapa[complex(i,j)] = '.'
    
    main(mapa)