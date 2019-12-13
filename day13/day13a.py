import sys
sys.path.append('..')
from collections import deque
from day9.day9b import program


def main(codes):
    # codes to dict
    memory = {i:v for i,v in enumerate(codes)}
    # print(list(program(memory, deque([1]))))
    read = deque()
    p = program(memory, read)
    tiles = {}
    try:
        while True:
            x,y,tile_id = [next(p) for _ in range(3)]
            tiles[(x,y)] = tile_id
    except StopIteration:
        print("painted", len(tiles))
        print("blocks", sum(1 for v in tiles.values() if v == 2))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)