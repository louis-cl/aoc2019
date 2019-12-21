import sys
from collections import deque
import heapq
import math
sys.path.append('..')
from day9.day9b import program
from utils import draw

def main(codes):
    memory = {i:v for i,v in enumerate(codes)}
    read = deque()
    p = program(memory, read)
    print(memory)

    mapa = {}
    count = 0
    for i in range(50):
        for j in range(50):
            z = complex(i,j)
            read = deque([i,j])
            p = program(memory.copy(), read)
            res = next(p)
            if res == 1:
                mapa[z] = '#'
                count += 1
    draw(mapa)
    print('count', count)



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    # h = len(lines)
    # w = len(lines[0])

    # mapa = {}
    # start = None
    # keys = set()
    # for i in range(h):
    #     for j in range(w):
    #         z = complex(i,j)
    #         c = lines[i][j]
    #         mapa[z] = c
    #         if c == '@':
    #             start = z
    #         elif c <= 'z' and c >= 'a':
    #             keys.add(c)

    main(codes)
    


