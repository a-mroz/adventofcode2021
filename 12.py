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

print(paths)
print(len(paths))