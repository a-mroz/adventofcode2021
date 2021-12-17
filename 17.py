min_x = 14
max_x = 50
min_y = -267
max_y = -255

# min_x = 20
# max_x = 30
# min_y = -10
# max_y = -5



def step(x, y, dx, dy):
    x += dx
    y += dy

    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1

    dy -= 1

    return x, y, dx, dy


def steps(dx, dy):
    x, y = 0, 0
    res = 0

    while y >= min_y:
    # while x <= max_x + 1 and y >= min_y - 1:
            x, y, dx, dy = step(x, y, dx, dy)
            print(x, y)
            res = max(res, y)

            if min_x <= x <= max_x and min_y <= y <= max_y:
                # print('hit', x, y)
                # print('min_y <= y <= max_y', min_y <= y <= max_y, min_y, y, max_y)
                return True, res
    return False, 0

max_height = 0

for vx in range(max_x + 1):
    for vy in range(-min_y):
# for vx in range(6, 7):
    # for vy in range(3, 4):
        hit, height = steps(vx, vy)
        if hit:
            # print(vx, vy, height)
            max_height = max(max_height, height)



print(max_height)