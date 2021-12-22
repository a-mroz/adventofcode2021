import fileinput
import re

input = []
for l in fileinput.input():
    # l = l.strip()
    # print(l)
    # print(re.findall(r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$', l))
    input.append(re.findall(r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$', l)[0])


turned_on = set()

print(input)

for on, x_min, x_max, y_min, y_max, z_min, z_max in input:
    x_min = int(x_min)
    x_max = int(x_max)
    y_min = int(y_min)
    y_max = int(y_max)
    z_min = int(z_min)
    z_max = int(z_max)


    if (x_min < -50 or x_min > 50) or (x_max < -50 or x_max > 50):
        print('skipping', x_min, x_max, y_min, y_max, z_min, z_max)
        continue

    print('procesing', x_min, x_max, y_min, y_max, z_min, z_max)


    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                if on == 'on':
                    turned_on.add((x, y, z))
                else:
                    turned_on.discard((x, y, z))

print(len(turned_on))