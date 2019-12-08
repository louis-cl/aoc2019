W = 25
H = 6
from collections import Counter

def main(codes):
    t = W*H
    n = len(codes)
    print('have', n / t)
    layers = []
    for i in range(100):
        layers.append(codes[150*i:150*i+150])

    min_0 = None
    layer = -1
    for l in layers:
        c = Counter(l)
        if min_0 == None or c[0] < min_0:
            min_0 = c[0]
            layer = l
    
    print(layer)
    c = Counter(layer)
    print("result", c[1]*c[2])


if __name__ == '__main__':
    with open('day8/input.txt', 'r') as f:
        lines = f.readlines()

    codes = lines[0]
    codes = list(map(int, codes))
    main(codes)