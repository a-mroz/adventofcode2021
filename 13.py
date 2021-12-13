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

# for (axis, coord) in folds:

axis, fold = folds[0]
GG = set()
maxY = max([y for _, y in G])
maxX = max([x for x, _ in G])

print(axis, fold)

if axis == 'y' and fold >= maxY / 2:
    for x, y in G:
        if y == fold:
            continue

        if y < fold:
            GG.add((x, y))
        else:
            yy = fold - abs(fold - y)
            GG.add((x, yy))

if axis == 'y' and fold < maxY / 2:
    for x, y in G:
        if y == fold:
            continue

        if y < fold:
            yy = y - fold + abs(fold - maxY)
            GG.add((x, yy))
        else:
            yy = maxY - y
            GG.add((x, yy))


# X

if axis == 'x' and fold >= maxX / 2:
    for x, y in G:
        if x == fold:
            continue

        if x < fold:
            GG.add((x, y))
        else:
            xx = fold - abs(fold - x)
            GG.add((xx, y))

if axis == 'x' and fold < maxX / 2:
    for x, y in G:
        if x == fold:
            continue

        if x < fold:
            xx = x - fold + abs(fold - maxX)
            GG.add((xx, y))
        else:
            xx = maxX - y
            GG.add((xx, y))



G = GG



print(len(G))