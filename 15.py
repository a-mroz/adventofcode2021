import fileinput
from collections import deque
import sys

G = []
for l in fileinput.input():
    G.append([int(x) for x in list(l.strip())])


R = len(G)
C = len(G[0])


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]




def dijkstra(G, start, end):
   seen = set()
   q = [(start, 0)] # TODO use a priority queue instead

   while q:
        node, dist = q.pop(0)
        if node == end:
           return dist

        if node in seen:
            continue

        seen.add(node)

        for neighbour_node, neighbour_dist in G[node]:
           q.append((neighbour_node, dist + neighbour_dist))

        q = sorted(q, key = lambda item: item[1]) # sort by dist



# part 1
graph = {}
for r in range(R):
    for c in range(C):
        links = []

        for i in range(4):
            rr = dr[i] + r
            cc = dc[i] + c

            if 0 <= rr < R and 0 <= cc < C:
                links.append(((rr, cc), G[rr][cc]))

            graph[(r, c)] = links

print(dijkstra(graph, (0, 0), (R - 1, C - 1)))

# part 2

# expand horizontally
for r in G:
    for i in range(1, 5):
        for c in range(C):
            new_c_idx = c + i * C
            previous_c_idx = new_c_idx - C

            r.append((r[previous_c_idx] + 1) % 10 or 1)

# expand vertically
for i in range(1, 5):
    for r in range(R):
        new_r_idx = r + i * R
        previous_r_idx = new_r_idx = new_r_idx - R

        G.append([(x + 1) % 10 or 1 for x in G[previous_r_idx]])

R = len(G)
C = len(G[0])

graph = {}
for r in range(R):
    for c in range(C):
        links = []

        for i in range(4):
            rr = dr[i] + r
            cc = dc[i] + c

            if 0 <= rr < R and 0 <= cc < C:
                links.append(((rr, cc), G[rr][cc]))

            graph[(r, c)] = links

print(dijkstra(graph, (0, 0), (R - 1, C - 1)))