import fileinput
from collections import defaultdict


G = defaultdict(set)

for l in fileinput.input():
    x, y = l.strip().split('-')
    G[x].add(y)
    G[y].add(x)


def dfs(u, visited, current_path, paths, visiting_condition):

    if u.islower():
        visited[u] += 1

    current_path.append(u)

    if u == 'end':
        paths.add(str(current_path))

        visited[u] -= 1
        current_path.pop()
        return

    for adj in G[u]:
        if visiting_condition(adj, visited):
            dfs(adj, visited, current_path, paths, visiting_condition)

    current_path.pop()

    if u.islower():
        visited[u] -= 1




# Part 1
paths = set()
dfs('start', defaultdict(int), [], paths, lambda cave, visited: cave.isupper() or visited[cave] < 1)
print(len(paths))


# Part 2

def can_go(cave, visited):
    if cave == 'start':
        return False

    if cave.isupper():
        return True

    if len(visited) == 0 or max(visited.values()) > 1:
        return visited[cave] < 1


    return visited[cave] < 2

paths = set()
dfs('start', defaultdict(int), [], paths, can_go)

print(len(paths))