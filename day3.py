import fileinput
from collections import Counter


def parse():
    return [l.strip() for l in fileinput.input()]


def task1(input):
    gamma = []
    epsilon = []


    for i in range(len(input[0])):
        ones = 0
        zeros = 0

        for l in input:
            if l[i] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

    return binaryToDec(gamma) * binaryToDec(epsilon)

def binaryToDec(arr):
    print(arr)
    mul = 1
    res = 0
    for i in range(len(arr) -1, -1, -1):

        res += mul * int(arr[i])
        mul *= 2
    return res


def task2(input):
    return binaryToDec(oxygen(0, input)) * binaryToDec(co2(0, input))


def oxygen(position, candidates):
    if len(candidates) == 1 or position >= len(candidates[0]):
        return list(candidates[0])

    counter = Counter()

    for l in candidates:
        counter.update(l[position])

    if counter['1'] >= counter['0']:
        return oxygen(position + 1, list(filter(lambda l: l[position] == '1', candidates)))
    else:
        return oxygen(position + 1, list(filter(lambda l: l[position] == '0', candidates)))



def co2(position, candidates):
    if len(candidates) == 1 or position >= len(candidates[0]):
        return list(candidates[0])

    counter = Counter()

    for l in candidates:
        counter.update(l[position])

    if counter['1'] < counter['0']:
        return co2(position + 1, list(filter(lambda l: l[position] == '1', candidates)))
    else:
        return co2(position + 1, list(filter(lambda l: l[position] == '0', candidates)))



input = parse()

print(task1(input))
print(task2(input))
