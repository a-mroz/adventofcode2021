import fileinput


def parse():
    return [int(l) for l in fileinput.input()]


def task1(input):
    previous_depth = None
    total_deeper = 0

    for depth in input:
        if previous_depth and depth > previous_depth:
            total_deeper += 1
        previous_depth = depth

    return total_deeper


def task2(input):
    previous_depth = None
    total_deeper = 0

    triplets = [input[i:i+3] for i in range(0, len(input))]
    for triplet in triplets:
        depth = sum(triplet)

        if previous_depth and depth > previous_depth:
            total_deeper += 1

        previous_depth = depth

    return total_deeper


input = parse()

print(task1(input))
print(task2(input))
