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


# ((r, c,), dist)
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



print(graph)

def dijkstra(G, start, end):
   seen = set()
   q = [(start, 0)]
#    q = deque()
#    q.append((start, 0))

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



print(dijkstra(graph, (0, 0), (R - 1, C - 1)))
