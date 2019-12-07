from collections import defaultdict, deque

def main(orbits):
    graph = defaultdict(list)

    for (s,t) in orbits:
        graph[s].append(t)
        graph[t].append(s)

    s = 'YOU'
    t = 'SAN'

    depth = {}
    queue = deque([s])
    depth[s] = 0
    while queue:
        v = queue.popleft()
        d = depth.get(v)+1
        for w in graph[v]:
            if w not in depth:
                depth[w] = d
                queue.append(w)

    print(depth[t] - 2)

if __name__ == '__main__':
    with open('day6/input.txt', 'r') as f:
        lines = f.readlines()

    def parse(line):
        line = line.strip()
        return (line[:3], line[4:])

    codes = list(map(parse, lines))
    main(codes)