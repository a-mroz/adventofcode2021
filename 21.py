from functools import lru_cache

def task1():

    p1 = 8
    p2 = 3
    s1 = 0
    s2 = 0

    die = 1

    rolls = 0


    p1_turn = True

    while s1 < 1000 and s2 < 1000:
        moves = 0
        for _ in range(3):
            moves += die
            die += 1
            rolls += 1

        if p1_turn:
            p1 += moves
            while p1 > 10:
                p1 -= 10
            s1 += p1

        else:
            p2 += moves
            while p2 > 10:
                p2 -= 10
            s2 += p2

        p1_turn = not p1_turn


    return rolls * min(s1, s2)

def task2():

    p1 = 8
    p2 = 3

    #example:
    # p1 = 4
    # p2 = 8
    print(max(dirac(True, p1, p2, 0, 0)))


DP = {}

@lru_cache(maxsize=None)
def dirac(p1_turn, p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    elif s2 >= 21:
        return (0, 1)


    ans = (0, 0)
    for r1 in range(1, 4):
        for r2 in range(1, 4):
            for r3 in range(1, 4):
                moves = r1 + r2 + r3

                if p1_turn:
                    new_p1 = p1 + moves
                    while new_p1 > 10:
                        new_p1 -= 10
                    win1, win2 = dirac(False, new_p1, p2, s1 + new_p1, s2)
                    ans = (ans[0] + win1, ans[1] + win2)

                else:
                    new_p2 = p2 + moves
                    while new_p2 > 10:
                        new_p2 -= 10

                    win1, win2 = dirac(True, p1, new_p2, s1, s2 + new_p2)
                    ans = (ans[0] + win1, ans[1] + win2)
    return ans



print(task1())
task2()
