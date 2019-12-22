import sys
from collections import deque
import heapq
import math
sys.path.append('..')
import re
import random


def integers(s):
    return re.findall(r'-?\d+', s.strip())

N = 119315717514047
K = 101741582076661
# N = 10
# K = 1

# Iterative Algorithm (xgcd)
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = iterative_egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m

def increment(pos, incr, inverses={}):
    # increment (incr*x) % N = pos
    # x = inv(incr) * pos % N
    if incr not in inverses:
        inverses[incr] = modinv(incr, N)
    inv = inverses[incr]
    x = inv*pos % N
    return x

def new_stack(pos):
    return N-1-pos

def cut(pos, x):
    return (pos + x) % N

def computeOps(lines):
    ops = []
    for line in lines:
        if line.startswith('deal with increment'):
            x = int(integers(line)[0])
            ops.append((0,x))
        elif line == 'deal into new stack':
            ops.append((1,None))
        elif line.startswith('cut'):
            x = int(integers(line)[0])
            ops.append((2,x))
        else:
            raise Exception('problem')
    return ops

def main(ops, pos):
    for k in range(1):
        for (op, x) in ops:
            if op == 0:
                pos = increment(pos, x)
            elif op == 1:
                pos = new_stack(pos)
            elif op == 2:
                pos = cut(pos, x)
            else:
                raise Exception('problem')
    return pos


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip('\n'), lines))
    lines.reverse()
    ops = computeOps(lines)
    
    # all operations are linear !!!
    # x = inv(incr) * y % N
    # x = N-1-y
    # x = (y + incr) % N
    
    # stop fucking optimizing and compose...
    # composition of linear ops in linear
    # f(x) is a*x + b % N

    f1 = main(ops, 2020) # f1 = a*2020 + b
    f2 = main(ops, f1)   # f2 = a*f1 + b
    diff = f2 - f1       # f2 - f1 = a*(f1 - 2020)
    print('f iterated', 2020, f1, f2)
    # a = (f2 - f1) * inv(f1-2020)
    a = (diff * modinv(f1-2020, N)) % N
    # b = f1 - a*2020
    b = (f1 - a * 2020) % N
    print(a, b)

    def g(x):
        return (a*x + b) % N

    # check a,b
    for i in range(100):
        x = random.randint(0,N-1)
        y1 = main(ops, x)
        y2 = g(x)
        if y1 != y2:
            raise Exception("WRONG")

    # compute g^K
    # g^2
    # a(ax+b)+b
    # a^2 x + ab + b

    # g^3
    # a^2 (ax + b) + ab + b
    # a^3 x + a^2 b + ab + b
    
    # g^k
    # a^k x + b * (a^(k-1) + ... + a + 1)

    # S = (a^(k-1) + ... + a + 1)
    # aS - S = a^k - 1
    # S = (a^k - 1)/(a-1)
    # S = a^k / (a-1)   -    1/(a-1)
    part1 = (pow(a,K,N) * 2020) % N
    invi = modinv(a-1, N)
    geo = (pow(a,K,N) * invi - invi) % N
    part2 = (b * geo) % N
    result = (part1 + part2) % N
    print('answer', result)