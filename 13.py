import fileinput

G = set()

folds = []

for l in fileinput.input():
    l = l.strip()

    if l == '':
        continue

    if l.startswith('fold along'):
        s1 = l.split('fold along')
        s2 = s1[1].split('=')
        folds.append((s2[0].strip(), int(s2[1])))
    else:
        s = l.split(',')
        G.add((int(s[0]), int(s[1])))

for i, (axis, fold) in enumerate(folds):
    maxY = max([y for _, y in G])
    maxX = max([x for x, _ in G])

    if axis == 'y':
        G = {(x,y) for x, y in G if y < fold} | {(x, fold - abs(fold - y)) for x, y in G if y > fold}
    else:
        G = {(x,y) for x, y in G if x < fold} | {(fold - abs(fold - x), y) for x, y in G if x > fold}

    #part 1
    if i == 0:
        print(len(G))


maxC = max([y for _, y in G])
maxR = max([x for x, _ in G])


for c in range(maxC + 1):
    for r in range(maxR + 1):
        if (r, c) in G:
            print('█', end = '')
        else:
            print(' ', end='')
    print('')
