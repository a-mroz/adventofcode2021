from collections import deque
import fileinput

G = []

for l in fileinput.input():
    G.append([int(d) for d in list(l.strip())])

dr = [-1, -1, -1, 0, 1, 1,  1,  0]
dc = [-1,  0,  1, 1, 1, 0, -1, -1]

R = len(G)
C = len(G[0])

flashes = 0


for _ in range(100):
    flashed = set()

    # step 1
    for r in range(R):
        for c in range(C):
            G[r][c] += 1


    # step 2, two parts
    q = deque()

    for r in range(R):
        for c in range(C):
            if G[r][c] > 9:
                flashed.add((r, c))

                for i in range(len(dr)):
                    rr = r + dr[i]
                    cc = c + dc[i]

                    if  0 <= rr < R and 0 <= cc < C:
                        G[rr][cc] += 1
                        q.append((rr, cc))


    while q:
        (r, c) = q.popleft()

        if (r, c) not in flashed and G[r][c] > 9:
            flashed.add((r, c))

            for i in range(len(dr)):
                rr = r + dr[i]
                cc = c + dc[i]

                if  0 <= rr < R and 0 <= cc < C:
                    G[rr][cc] += 1
                    q.append((rr, cc))


    # step 3
    for r, c in flashed:
        G[r][c] = 0

    flashes += len(flashed)

    # print('\n')
    # print(G)
    # print(flashes)



print(flashes)