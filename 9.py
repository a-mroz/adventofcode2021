import fileinput


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
    pass

input = parse()

print(task1(input))
print(task2(input))
