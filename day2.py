import fileinput


def parse():
    return [l.split() for l in fileinput.input()]


def task1(input):
    horizontal = 0
    depth = 0

    for cmd in input:
        dir = cmd[0]
        val = int(cmd[1])

        if dir == 'forward':
            horizontal += val
        if dir == 'down':
            depth += val
        if dir == 'up':
            depth -= val

    return horizontal * depth


def task2(input):
    horizontal = 0
    depth = 0
    aim = 0

    for cmd in input:
        dir = cmd[0]
        val = int(cmd[1])

        if dir == 'forward':
            horizontal += val
            depth += aim * val
        if dir == 'down':
            aim += val
        if dir == 'up':
            aim -= val

    return horizontal * depth


input = parse()

print(task1(input))
print(task2(input))
