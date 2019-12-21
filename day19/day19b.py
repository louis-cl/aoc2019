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

    def check(z):
        read = deque([int(z.real),int(z.imag)])
        p = program(memory.copy(), read)
        res = next(p)
        return res == 1


    for x in range(20):
        for y in range(20):
            z = complex(x,y)
            if check(z):
                mapa[z] = '#'
    draw(mapa)


    # follow top part of beam
    z = complex(200,0)
    while True:
        while not check(z):
            z += complex(0,1)
        # print('found ', z)
        bottom_left = z + complex(-99, 99)
        if check(bottom_left):
            top_left = complex(min(z.real, bottom_left.real), min(z.imag, bottom_left.imag))
            print('probably found', top_left)
            break
        z += complex(1,0)
        while check(z):
            z += complex(1,0)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)