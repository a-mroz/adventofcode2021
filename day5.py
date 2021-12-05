import fileinput
from collections import Counter
from collections import defaultdict

import re

def parse():
    res = []
    for l in fileinput.input():
        matches = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', l)
        res.append([(int(x1), int(y1), int(x2), int(y2)) for (x1, y1, x2, y2) in matches])

    return res


def task1(input):
    points = []

    for stream  in input:
        x1, y1, x2, y2 = stream[0]

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points.append((x, y1))
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, y))

    return len({x for x, count in Counter(points).items() if count > 1})


def task2(input):
    points = []

    for stream  in input:
        x1, y1, x2, y2 = stream[0]

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points.append((x, y1))
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, y))
        elif x2 > x1 and y2 > y1:
            for i in range(y2 - y1 + 1):
                points.append((x1 + i, y1 + i))
        elif x2 > x1 and y2 < y1:
            for i in range(abs(y2 - y1) + 1):
                points.append((x1 + i, y1 - i))
        elif x2 < x1 and y2 > y1:
            for i in range(y2 - y1 + 1):
                points.append((x1 - i, y1 + i))
        elif x2 < x1 and y2 < y1:
            for i in range(abs(y2 - y1) + 1):
                points.append((x1 - i, y1 - i))
        else:
            print('Error')

    print(points)

    return len({x for x, count in Counter(points).items() if count > 1})


input = parse()

print(task1(input))
print(task2(input))
