def parse(str):
    return (str[0], int(str[1:]))

dirs = {
    'U': (0,1),
    'R': (1,0),
    'L': (-1,0),
    'D': (0,-1)
}

def add(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def dist(t1):
    (a,b) = t1
    return abs(a) + abs(b)

def main(w1, w2):
    # mark wire 1 positions
    marked = {}
    point = (0,0)
    steps = 0
    for (d, l) in w1:
        diri = dirs[d]
        for i in range(1,l+1):
            point = add(point, diri)
            steps += 1
            if point not in marked:
                marked[point] = steps
    
    # check wire 2 overlapping
    point = (0,0)
    steps = 0
    min_cross = (0,0)
    min_steps = -1
    for (d, l) in w2:
        diri = dirs[d]
        for i in range(1,l+1):
            point = add(point, diri)
            steps += 1
            if point in marked:
                sum_steps = steps + marked[point]
                if sum_steps < min_steps or min_steps == -1:
                    min_steps = sum_steps
                    min_cross = point
    
    print(min_cross, min_steps)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')
    wire1 = list(map(parse, wire1))
    wire2 = list(map(parse, wire2))
    main(wire1, wire2)