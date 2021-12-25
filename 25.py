import fileinput


def parse():
    grid = []
    for line in fileinput.input():
        grid.append(list(line.strip()))

    return grid


grid = parse()


still_moving = True
steps = 0


while still_moving:
    still_moving = False
    new_grid = [row[:] for row in grid]

    # move to east
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == '>':
                row_to_check = i
                col_to_check = j + 1 if j + 1 < len(r) else 0

                # check if it can move
                if grid[row_to_check][col_to_check] == '.':
                    new_grid[i][j] = '.'
                    new_grid[row_to_check][col_to_check] = '>'
                    still_moving = True


    newer_grid = [row[:] for row in new_grid]

    # move to south
    for i, r in enumerate(new_grid):
        for j, c in enumerate(r):
            if c == 'v':
                row_to_check = i + 1 if i + 1 < len(new_grid) else 0
                col_to_check = j

                # check if it can move
                if new_grid[row_to_check][col_to_check] == '.':
                    newer_grid[i][j] = '.'
                    newer_grid[row_to_check][col_to_check] = 'v'
                    still_moving = True


    grid = newer_grid
    steps += 1
    # print(steps)
    # if steps == 1:
        # for r in grid:
            # print(''.join(r))
        # break

print()
for r in grid:
    print(''.join(r))

print(steps)
