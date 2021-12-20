import fileinput
import copy

def parse():
    algorithm = None
    grid = set()

    for r, l in enumerate(fileinput.input()):
        l = l.strip()

        if not algorithm:
            algorithm = l
        elif not l:
            continue
        else:
            for c, v in enumerate(l):
                if v == '#':
                    grid.add((r, c))

    return algorithm, grid


dr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def play(round, algorithm, grid):
    G = set()
    max_r = max([r for r, c in grid])
    min_r = min([r for r, c in grid])
    max_c = max([c for r, c in grid])
    min_c = min([c for r, c in grid])


    for r in range(min_r - 5, max_r + 10):
        for c in range(min_c - 5, max_c + 10):
            binary = ''

            for i in range(len(dr)):
                rr = dr[i] + r
                cc = dc[i] + c

                if (rr, cc) in grid:
                    binary += '1'
                elif min_r <= rr <= max_r and min_c <= cc <= max_c:
                    # In the grid, but dark
                    binary += '0'
                else:
                    # Out of the grid, it depends on what round it is
                    # symbol = algorithm[0] if round % 2 == 0 else algorithm[-1]
                    # binary += '1' if symbol == '#' else '0'
                    binary += str(round % 2)

            if algorithm[int(binary, 2)] == '#':
                G.add((r, c))

    return G


def task1():
    algorithm, grid = parse()

    print_grid(grid)
    print('')

    for round in range(2):
        grid = play(round, algorithm, grid)
        print_grid(grid)
        print('')

    return len(grid)


def print_grid(grid):
    max_r = max([r for r, c in grid])
    min_r = min([r for r, c in grid])
    max_c = max([c for r, c in grid])
    min_c = min([c for r, c in grid])


    for r in range(min_r - 5, max_r + 5):
        row = []
        for c in range(min_c - 5, max_c + 5):
            row.append('#' if (r, c) in grid else '.')
        print(''.join(row))



print(task1())