import re
import sys
from dataclasses import dataclass

from math import gcd 
from functools import reduce
def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

@dataclass
class Moon:
    pos: list
    vel: list

def step(moons):
    # apply gravity
    # print("bef", moons)
    for m1 in moons:
        for m2 in moons:
            for i in range(3):
                if m1.pos[i] == m2.pos[i]:
                    continue
                elif m1.pos[i] > m2.pos[i]:
                    m1.vel[i] -= 1
                else: # m1.pos[i] < m2.pos[i]:
                    m1.vel[i] += 1
    # print("aft", moons)
    # update pos
    for m1 in moons:
        m1.pos = [a+b for (a,b) in zip(m1.pos, m1.vel)]

def energy(moon):
    sumabs = lambda y: sum(abs(x) for x in y)
    return sumabs(moon.pos) * sumabs(moon.vel)

def main(moons):
    # find cycle per coordinate 
    hashi = lambda i: tuple((m.pos[i], m.vel[i]) for m in moons)
    objective = [hashi(i) for i in range(3)]
    steps = [None]*3
    time = 0
    while not all(steps):
        step(moons)
        time += 1
        for i in range(3):
            if not steps[i]:
                if hashi(i) == objective[i]:
                    steps[i] = time

    print("cycles", steps)
    print("answer", lcm(steps))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    moons = []
    for line in lines:
        nums = [int(s) for s in re.findall(r'-?\d+', line.strip())]
        moons.append(Moon(nums, [0,0,0]))
    
    main(moons)