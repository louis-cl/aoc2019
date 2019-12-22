import sys
from collections import deque
import heapq
import math
sys.path.append('..')
from utils import integers

N = 10

def increment(cards, incr):
    res = cards.copy()
    k = 0
    while cards:
        res[k] = cards.popleft()
        k = (k + incr) % len(res)
    return res

def new_stack(cards):
    cards.reverse()
    return cards

def cut(cards, x):
    cards.rotate(-x)
    return cards

def main(lines):
    cards = deque(list(range(N)))
    for line in lines:
        if line.startswith('deal with increment'):
            x = int(integers(line)[0])
            print('increment', x)
            cards = increment(cards, x)
        elif line == 'deal into new stack':
            print('new stack')
            cards = new_stack(cards)
        elif line.startswith('cut'):
            x = int(integers(line)[0])
            print("cut", x)
            cards = cut(cards, x)
        else:
            raise Exception('problem')
        print(cards)

    for i,x in enumerate(cards):
        if x == 2019:
            print('position', i)
            break


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip('\n'), lines))
    print(lines)
    main(lines)
