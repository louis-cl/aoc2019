import sys
from collections import deque
sys.path.append('..')

dirs = [
    complex(1,0),
    complex(0,1),
    complex(-1,0),
    complex(0,-1)
]

def in_map(z):
    t = [z.real, z.imag]
    return all(c in range(5) for c in t)

def n_adj_in(mapa, d, lvl):
    count = 0

    def add(lvl, z):
        return 1 if mapa.get((lvl, z), '.') == '#' else 0

    if d == complex(1,0):
        for i in range(5):
            count += add(lvl+1, complex(0,i))
    elif d == complex(-1,0):
        for i in range(5):
            count += add(lvl+1, complex(4,i))
    elif d == complex(0,1):
        for i in range(5):
            count += add(lvl+1, complex(i,0))
    elif d == complex(0,-1):
        for i in range(5):
            count += add(lvl+1, complex(i,4))
    else:
        raise Exception('unknown dir')
    return count
            
def n_adj_out(mapa, d, lvl):
    z = complex(2,2) + d
    return 1 if mapa.get((lvl-1, z), '.') == '#' else 0

def n_adj(mapa, p, lvl):
    neigh = 0
    for d in dirs:
        z = p + d
        if z == complex(2,2):
            neigh += n_adj_in(mapa, d, lvl)
        elif not in_map(z):
            neigh += n_adj_out(mapa, d, lvl)
        else:
            if mapa[lvl, z] == '#':
                neigh += 1
    return neigh

def step(mapa):
    map2 = {}
    for lvl,z in mapa:
        if z == complex(2,2):
            continue
        n = n_adj(mapa, z, lvl)
        if mapa[lvl, z] == '#':
            map2[lvl, z] = '#' if n == 1 else '.'
        else:
            map2[lvl, z] = '#' if n in [1,2] else '.'
    return map2

def draw2(mapa):
    rngs = [k for (k, _) in mapa.keys()]
    for lvl in range(min(rngs), max(rngs)+1):
        print('level', lvl)
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    print('?', end='')
                else:
                    print(mapa[(lvl, complex(i,j))], end='')
            print()
    print()

def main(mapa):
    draw2(mapa)
    for epoch in range(200):
        print('EPOCH', epoch+1)
        # put empty lvls ?
        lvls = [k for (k, _),c in mapa.items() if c == '#']
        rng = [min(lvls)-1, max(lvls)+1]
        for lvl in rng:
            for i in range(5):
                for j in range(5):
                    mapa[lvl, complex(i,j)] = '.'
    
        mapa = step(mapa)
        # draw2(mapa)
    res = sum(1 for _,c in mapa.items() if c == '#')
    print("BUGS", res)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip('\n'), lines))
    mapa = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                mapa[(0,complex(i,j))] = '#'
            else:
                mapa[(0,complex(i,j))] = '.'
    main(mapa)