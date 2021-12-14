from collections import Counter
import fileinput


def diff_single_letters(counter):
    single = Counter()
    for k, v in counter.items():
        single[k[0]] += v
    single[start[-1]] += 1
    return single.most_common()[0][1] - single.most_common()[-1][1]

start = None
rules = {}

for l in fileinput.input():
    l = l.strip()

    if start == None:
        start = list(l)
        continue

    if l == '':
        continue

    s = l.split(' -> ')

    rules[s[0]] = s[1]
    # rules.append((s[0], s[1]))

res = list(start)


c = Counter( (a+b) for a,b in zip(res, res[1:]))

for i in range(40):
    cc = Counter()

    for pair, cnt in c.items():
        middle = rules[pair]
        cc[pair[0] + middle] += cnt
        cc[middle + pair[1]] += cnt

    c = cc

    if i == 9:
        print(diff_single_letters(c))

print(diff_single_letters(c))
