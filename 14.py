from collections import Counter
import fileinput

G = set()

folds = []


start = None
rules = []

for l in fileinput.input():
    l = l.strip()

    if start == None:
        start = l
        continue

    if l == '':
        continue

    s = l.split(' -> ')

    rules.append((s[0], s[1]))

res = list(start)

for i in range(40):

    n = []
    for a, b in zip(res, res[1:]):
        n.append(a)
        for r1, r2 in rules:
            if r1[0] == a and r1[1] == b:
                # print(a, b, '-> ', r1, r2)
                n.append(r2)

    n.append(res[-1])
    res = n

    print(i)

c = Counter(res)
print(c.most_common())
print(c.most_common()[0][1] - c.most_common()[-1][1])