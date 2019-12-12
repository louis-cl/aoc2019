import sys
import re
from dataclasses import dataclass

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
    # print(moons)
    # update pos
    for m1 in moons:
        m1.pos = [a+b for (a,b) in zip(m1.pos, m1.vel)]


def energy(moon):
    sumabs = lambda y: sum(abs(x) for x in y)
    return sumabs(moon.pos) * sumabs(moon.vel)


def main(moons):
    for _ in range(1000):
        step(moons)

    en = sum(map(energy, moons))
    print("energy", en)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    moons = []
    for line in lines:
        nums = [int(s) for s in re.findall(r'-?\d+', line.strip())]
        moons.append(Moon(nums, [0,0,0]))
    
    main(moons)