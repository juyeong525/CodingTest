import sys
from collections import deque

def dfs(graph, start):
    visited = set()
    stack = deque([start])
    line = [0] * (len(graph))
    count = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            count += 1
            line[node - 1] = count
            stack.extend(sorted(graph[node], reverse=True))

    return line

n, m, r = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(graph, r)

for l in result:
    print(l)
