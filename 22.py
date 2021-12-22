import fileinput
import re
import collections


def parse():
    input = []
    for l in fileinput.input():
        input.append(re.findall(r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$', l)[0])
    return input


def part1(instructions):
    turned_on = set()

    for on, x_min, x_max, y_min, y_max, z_min, z_max in instructions:
        x_min = int(x_min)
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)
        z_min = int(z_min)
        z_max = int(z_max)

        if (x_min < -50 or x_min > 50) or (x_max < -50 or x_max > 50):
            continue

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    if on == 'on':
                        turned_on.add((x, y, z))
                    else:
                        turned_on.discard((x, y, z))

    print(len(turned_on))


def part2(instructions):

    cubes = []

    for on, x_min, x_max, y_min, y_max, z_min, z_max in instructions:
        x_min = int(x_min)
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)
        z_min = int(z_min)
        z_max = int(z_max)

        # check for overlaps
        new_cubes = cubes[:]
        for (cx_min, cx_max, cy_min, cy_max, cz_min, cz_max), sgn in cubes:
            x_overlaps = not (x_max < cx_min or x_min > cx_max)
            y_overlaps = not (y_max < cy_min or y_min > cy_max)
            z_overlaps = not (z_max < cz_min or z_min > cz_max)

            # x_overlaps = cx_min <= x_min <= cx_max or cx_min <= x_max <= cx_max
            # y_overlaps = cy_min <= y_min <= cy_max or cy_min <= y_max <= cy_max
            # z_overlaps = cz_min <= z_min <= cz_max or cz_min <= z_max <= cz_max


            if x_overlaps and y_overlaps and z_overlaps:
                # cubes overlap, we have to substract from them, we're looking for a small cube - intersection of these two

                intersection_x_min = max(x_min, cx_min)
                intersection_x_max = min(x_max, cx_max)

                intersection_y_min = max(y_min, cy_min)
                intersection_y_max = min(y_max, cy_max)

                intersection_z_min = max(z_min, cz_min)
                intersection_z_max = min(z_max, cz_max)

                # sgn - what was already lit (integer)
                # on - the new, incoming one (bool)
                # If previous was lit, we want to turn it off
                # if it was not lit, then it depends if the current one tries to turn it on or off
                sign = None
                if sgn == 1:
                    sign = -1
                elif on:
                    sign = 1
                else:
                    sign = -1

                new_cubes.append(((intersection_x_min, intersection_x_max,
                                    intersection_y_min, intersection_y_max,
                                    intersection_z_min, intersection_z_max), sign))

        if on == 'on':
            new_cubes.append(((x_min, x_max, y_min, y_max, z_min, z_max), 1))

        cubes = new_cubes

    return sum([(x2 - x1 + 1 ) * (y2 - y1 + 1) * (z2 - z1 + 1) * sgn  for (x1, x2, y1, y2, z1, z2), sgn in cubes])



instructions = parse()
part1(instructions)
print(part2(instructions))
