import fileinput
from collections import Counter

def parse():
    for l in fileinput.input():
       return [int(f) for f in l.split(',')]

# Naive approach
def task1(fishes):
    for day in range(80):
        fishes_to_be_added = 0
        for i, f in enumerate(fishes):
            if f == 0:
                fishes_to_be_added += 1
                fishes[i] = 6
            else:
                fishes[i] = f - 1
        fishes.extend([8] * fishes_to_be_added)

    return len(fishes)

# I got this idea on Reddit.
# We don't need actual fishes, just the number of them. Brilliant.
# Otherwise, it becomes too big pretty fast
def task2(fishes):
    for i in range(256):
        new_gen = Counter()

        for age, number in fishes.most_common():
            if age <= 0:
                new_gen[6] += number
                new_gen[8] += number
            else:
                new_gen[age - 1] += number
        fishes = new_gen


    return sum([number for _, number in fishes.most_common()])

input = parse()

print(task1(input.copy()))
print(task2(Counter(input)))
