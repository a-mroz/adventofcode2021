
p1 = 8
p2 = 3
# p1 = 4
# p2 = 8

s1 = 0
s2 = 0

die = 1

rolls = 0


p1_turn = True

while s1 < 1000 and s2 < 1000:
    moves = 0
    for _ in range(3):
        moves += die
        print(die)
        die += 1
        rolls += 1

    if p1_turn:
        p1 += moves
        while p1 > 10:
            p1 -= 10
        s1 += p1
        print('p1', p1, s1)

    else:
        p2 += moves
        while p2 > 10:
            p2 -= 10
        s2 += p2
        print('p2', p2, s2)

    print()
    p1_turn = not p1_turn

print(s1, s2)
print(rolls)


res = rolls * min(s1, s2)

print(res)