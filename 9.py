import fileinput
import math
from collections import deque

def parse():
    map = []
    for l in fileinput.input():
        map.append([int(f) for f in l.strip()])
    return map

def task1(map):
    lowest = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            candidate = map[row][col]

            if row > 0 and map[row - 1][col] <= candidate:
                continue
            if row < len(map) - 1 and map[row + 1][col] <= candidate:
                continue
            if col > 0 and map[row][col - 1] <= candidate:
                continue
            if col < len(map[row]) - 1 and map[row][col + 1] <= candidate:
                continue

            lowest.append(candidate)

    return sum([l +1 for l in lowest])


def task2(map):
    basins = []
    seen = set()

    dr = [-1, 0, 1, 0] # delta rows
    dc = [0, 1, 0, -1] # delta columns

    # borders
    R = len(map)
    C = len(map[0])

    for r in range(R):
        for c in range(C):
            if (r, c) not in seen and map[r][c] != 9:
                basin = 0
                q = deque()
                q.append((r, c))
                while q:
                    (r, c) = q.popleft()
                    if (r, c) in seen:
                        continue
                    basin += 1
                    seen.add((r, c))

                    for d in range(len(dr)):
                        # candidates
                        rr = r + dr[d]
                        cc = c + dc[d]

                        # if it's in the grid
                        if 0 <= rr < R and 0 <= cc < C and map[rr][cc] != 9:
                            q.append((rr, cc))

                basins.append(basin)


    return math.prod(sorted(basins, reverse = True)[:3])


input = parse()

print(task1(input))
print(task2(input))
