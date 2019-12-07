from collections import defaultdict

def dfs(u, visited, graph, stack):
    visited.add(u)
    for v in graph.get(u, []):
        if v not in visited:
            dfs(v, visited, graph, stack)
    stack.append(u)

def top_sort(graph):
    stack = []
    visited = set()
    for v in graph.keys():
        if v not in visited:
            dfs(v, visited, graph, stack)
    return stack

def main(orbits):
    graph = defaultdict(list)
    parentOf = {}

    for (s,t) in orbits:
        graph[s].append(t)
        parentOf[t] = s
    
    order = top_sort(graph)
    order.reverse()

    countOf = defaultdict(lambda: 0)
    for p in order:
        if p in parentOf:
            parent = parentOf[p]
            countOf[p] = countOf[parent] + 1
            
    result = sum(countOf.values())
    print(result)

if __name__ == '__main__':
    with open('day6/input.txt', 'r') as f:
        lines = f.readlines()

    def parse(line):
        line = line.strip()
        return (line[:3], line[4:])

    codes = list(map(parse, lines))
    main(codes)