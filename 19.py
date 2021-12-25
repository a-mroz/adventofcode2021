import fileinput
from itertools import permutations


def parse():
    scanners = []

    buffer = []

    for l in fileinput.input():
        l = l.strip()
        if l.startswith('---'):
            continue
        if l == '':
            scanners.append(buffer)
            buffer = []
        else:
            s = l.split(',')
            buffer.append((int(s[0]), int(s[1]), int(s[2])))
    scanners.append(buffer)

    return scanners

def rotate(x, y, z):
    def spin_right(x, y, z):
        return y, x, z

    def spin_up(x, y, z):
        return


def rotations(points):
    # for x in [(x, y, z) for permutations(x, y, z) in points]:
    #     yield x

    # for x in permutations([(-x, y, z) for x, y, z in points]):
    #     yield x

    # for x in permutations([(x, -y, z) for x, y, z in points]):
    #     yield x

    # for x in permutations([(x, y, -z) for x, y, z in points]):
    #     yield x

    # for x in permutations([(-x, -y, z) for x, y, z in points]):
    #     yield x

    # for x in permutations([(x, -y, -z) for x, y, z in points]):
    #     yield x

    # for x in permutations([(-x, y, -z) for x, y, z in points]):
    #     yield x

    # for x in permutations([(-x, -y, -z) for x, y, z in points]):
    #     yield x


    yield [(x, y, z) for x, y, z in points]
    yield [(-x, y, z) for x, y, z in points]
    yield [(x, -y, z) for x, y, z in points]
    yield [(x, y, -z) for x, y, z in points]
    yield [(-x, -y, z) for x, y, z in points]
    yield [(-x, y, -z) for x, y, z in points]
    yield [(x, -y, -z) for x, y, z in points]
    yield [(-x, -y, -z) for x, y, z in points]

    yield [( x,  z,  y) for x, y, z in points]
    yield [(-x,  z,  y) for x, y, z in points]
    yield [( x,  z, -y) for x, y, z in points]
    yield [( x, -z,  y) for x, y, z in points]
    yield [(-x,  z, -y) for x, y, z in points]
    yield [(-x, -z,  y) for x, y, z in points]
    yield [( x, -z, -y) for x, y, z in points]
    yield [(-x, -z, -y) for x, y, z in points]


    yield [( y,  x,  z) for x, y, z in points]
    yield [( y, -x,  z) for x, y, z in points]
    yield [(-y,  x,  z) for x, y, z in points]
    yield [( y,  x, -z) for x, y, z in points]
    yield [(-y, -x,  z) for x, y, z in points]
    yield [( y, -x, -z) for x, y, z in points]
    yield [(-y,  x, -z) for x, y, z in points]
    yield [(-y, -x, -z) for x, y, z in points]

    yield [( y,  z,  x,) for x, y, z in points]
    yield [( y,  z, -x,) for x, y, z in points]
    yield [(-y,  z,  x,) for x, y, z in points]
    yield [( y, -z,  x,) for x, y, z in points]
    yield [(-y,  z, -x,) for x, y, z in points]
    yield [( y, -z, -x,) for x, y, z in points]
    yield [(-y, -z,  x,) for x, y, z in points]
    yield [(-y, -z, -x,) for x, y, z in points]

    yield [( z,  x,  y) for x, y, z in points]
    yield [( z, -x,  y) for x, y, z in points]
    yield [( z,  x, -y) for x, y, z in points]
    yield [(-z,  x,  y) for x, y, z in points]
    yield [( z, -x, -y) for x, y, z in points]
    yield [(-z, -x,  y) for x, y, z in points]
    yield [(-z,  x, -y) for x, y, z in points]
    yield [(-z, -x, -y) for x, y, z in points]

    yield [( z,  y,  x) for x, y, z in points]
    yield [( z,  y, -x) for x, y, z in points]
    yield [( z, -y,  x) for x, y, z in points]
    yield [(-z,  y,  x) for x, y, z in points]
    yield [( z, -y, -x) for x, y, z in points]
    yield [(-z,  y, -x) for x, y, z in points]
    yield [(-z, -y,  x) for x, y, z in points]
    yield [(-z, -y, -x) for x, y, z in points]




def find_match(known_scanners, known_coords, scanners):
    for i in range(len(scanners)):
        if i in known_scanners:
            continue
        # TODO for all orientations:

        for rotated in rotations(scanners[i]):
            for idx_known, (kx, ky, kz) in enumerate(known_coords):
                for idx_test, (tx, ty, tz) in enumerate(rotated):
                    # for a given known coord, we're checking all points for a testing scanner
                    # we calculate delta and then we check
                    dx, dy, dz = kx - tx, ky - ty, kz - tz

                    matches = 0
                    for (t2x, t2y, t2z) in rotated: #[idx2+ 1:]
                        if (t2x + dx, t2y + dy, t2z + dz) in known_coords:
                            matches += 1

                    if matches >= 12:
                        # we have a match for a given scanner, and we known the transformed coords
                        return i, [(x + dx, y + dy, z + dz) for (x, y, z) in rotated], dx, dy, dz

    assert False # shouldn't reach here


def manhattan(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def task1():
    scanners = parse()

    final_scanners = [None for x in scanners]
    final_scanners[0] = (0, 0, 0)

    known_scanners = set()
    known_scanners.add(0)

    known_coords = set()
    known_coords |= set(scanners[0])

    while len(known_scanners) < len(scanners):
        matched_idx, matched_coords, dx, dy, dz = find_match(known_scanners, known_coords, scanners)
        known_scanners.add(matched_idx)
        known_coords |= set(matched_coords)
        final_scanners[matched_idx] = (dx, dy, dz)

    print(len(known_coords))

    print(final_scanners)


    max_manhattan = float('-inf')
    for s1 in final_scanners:
        for s2 in final_scanners:
            max_manhattan = max(manhattan(s1, s2), max_manhattan)

    print(max_manhattan)


task1()