import fileinput
from collections import defaultdict


G = defaultdict(set)

for l in fileinput.input():
    x, y = l.strip().split('-')
    G[x].add(y)
    G[y].add(x)




paths = set()

def dfs(u, visited, current_path):

    if u.islower():
        visited.add(u)

    current_path.append(u)

    if u == 'end':
        # print(current_path)
        paths.add(str(current_path))

        visited.remove(u)
        current_path.pop()
        return

    for adj in G[u]:
        if adj not in visited:
            dfs(adj, visited, current_path)

    current_path.pop()

    if u.islower():
        visited.remove(u)


dfs('start', set(), [])

print(len(paths))



paths = set()

def dfs2(u, visited, current_path):

    if u.islower():
        visited[u] += 1


    current_path.append(u)

    if u == 'end':
        # print(current_path)
        paths.add(str(current_path))

        visited[u] -= 1
        current_path.pop()
        return

    for adj in G[u]:
        # if adj not in visited:
        # if adj.isupper() or (len(adj) == 1 and visited[adj] < 2) or (visited[adj] < 1):
        if can_go(adj, visited):
        # if (len(adj) == 1 and visited[adj] < 2)  and adj != 'start':
            dfs2(adj, visited, current_path)

    current_path.pop()

    if u.islower():
        visited[u] -= 1


def can_go(cave, visited):
    if cave == 'start':
        return False

    if cave.isupper():
        return True

    if len(visited) == 0 or max(visited.values()) > 1:
        return visited[cave] < 1


    return visited[cave] < 2






dfs2('start', defaultdict(int), [])

# print(paths)
print(len(paths))