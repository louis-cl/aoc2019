import sys
sys.path.append('..')
from utils import lcm, integers
from collections import deque
from day9.day9b import program

def draw(tiles):
    max_y = max(y for (_,y) in tiles.keys())
    max_x = max(x for (x,_) in tiles.keys())

    tileset = {
        0: ' ',
        1: '#',
        2: 'b',
        3: '-',
        4: 'o'
    }

    for j in range(max_y):
        for i in range(max_x):
            if (i,j) in tiles:
                print(tileset[tiles[(i,j)]], end='')
            else:
                print(' ', end='')
        print()

class AI:
    def __init__(self, tiles):
        self.tiles = tiles

    def popleft(self):
        # draw(self.tiles)
        # print("ball", self.ball)
        # print("paddle", self.paddle)
        # stupid ai following the ball...
        if self.ball.real < self.paddle.real:
            return -1
        elif self.ball.real > self.paddle.real:
            return 1
        else:
            return 0
    
    def setBall(self, p):
        x,y = p
        self.ball = complex(x,y)

    def setPaddle(self, p):
        x,y = p
        self.paddle = complex(x,y)


def main(codes):
    # codes to dict
    memory = {i:v for i,v in enumerate(codes)}
    # print(list(program(memory, deque([1]))))
    read = deque()
    p = program(memory.copy(), read)
    tiles = {}
    info = {}
    try:
        while True:
            x = next(p)
            y = next(p)
            tile_id = next(p)
            if tile_id == 4:
                info['ball'] = (x,y)
            elif tile_id == 3:
                info['paddle'] = (x,y)
            tiles[(x,y)] = tile_id
            # print("new pos", pos)
    except StopIteration:
        print("blocks", sum(1 for v in tiles.values() if v == 2))
    
    draw(tiles)

    # part 2
    memory[0] = 2 # play for free
    read = AI(tiles)
    read.setBall(info['paddle'])
    read.setBall(info['ball'])

    p = program(memory, read)
    try:
        while True:
            x = next(p)
            y = next(p)
            tile_id = next(p)
            if x == -1 and y == 0:
                print("score", tile_id)
            else:
                tiles[(x,y)] = tile_id

            if tile_id == 4:
                read.setBall((x,y))
            elif tile_id == 3:
                read.setPaddle((x,y))
    except StopIteration:
        print("blocks", sum(1 for v in tiles.values() if v == 2))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    codes = lines[0].split(',')
    codes = list(map(int, codes))
    main(codes)