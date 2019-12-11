from collections import deque, defaultdict
import sys
sys.path.append('..')
from day9.day9b import program

def main(codes):
    # codes to dict
    memory = {i:v for i,v in enumerate(codes)}
    # print(list(program(memory, deque([1]))))
    mapa = defaultdict(lambda: False) # True if white, False if black
    pos = complex(0,0)

    dirs = [complex(0,1), complex(1,0), complex(0,-1), complex(-1,0)]
    facingIdx = 0 # up

    def get(p):
        return 1 if mapa[p] else 0

    read = deque()
    p = program(memory, read)

    try:
        while True:
            # give input to the program
            v = get(pos)
            read.append(v)
            # get color to paint
            color = next(p)
            # print("GOT COLOR", color)
            # paint
            mapa[pos] = color == 1

            diri  = next(p)
            # print("GOT DIR", diri)
            # rotate
            if diri == 0: # left
                facingIdx = (facingIdx - 1) % 4
            else:
                facingIdx = (facingIdx + 1) % 4
            # update pos
            pos += dirs[facingIdx]
            # print("new pos", pos)
    except StopIteration:
        # done with colors
        print("painted", len(mapa))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)