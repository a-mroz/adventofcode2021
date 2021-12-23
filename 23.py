
# Watch out!
# I started an implementation, but gave up and did it manually
# The implementation is probably some variation of Dijkstra, but it coding rules of movement might be kind of hard....

a = 1
b = 10
c = 100
d = 1000

map = """
#############
#...........#
###B#D#C#A###
  #C#D#B#A#
  #########
"""

# part 1
"""
#############
#.A.......A.# 2A + 9A
###B#D#C#.###
  #C#D#B#.#
  #########


#############
#.A.......A.# 7D + 7D
###B#.#C#D###
  #C#.#B#D#
  #########


#############
#.A.....C.A.# 2C
###B#.#.#D###
  #C#.#B#D#
  #########

#############
#.A.....C.A.# 5B + 5B
###.#B#.#D###
  #C#B#.#D#
  #########

#############
#.A.......A.# 3C + 7C
###.#B#C#D###
  #.#B#C#D#
  #########


#############
#...........# 3A + 8A
###A#B#C#D###
  #A#B#C#D#
  #########

"""

print('Part 1', a * 2 + 9 * a + 7 * d + 7 * d + 2 * c + 10 * b + 10 * c + 11 * a)

# part 2

"""

#############
#...........# D7
###B#D#C#A###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#B#A#
  #########

#############
#..........D# C5
###B#.#C#A###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#B#A#
  #########


#############
#.C........D# 4B
###B#.#C#A###
  #D#.#B#A#
  #D#B#A#C#
  #C#D#B#A#
  #########


#############
#.C.B......D# 9D
###B#.#C#A###
  #D#.#B#A#
  #D#.#A#C#
  #C#D#B#A#
  #########

#############
#.C.B.....DD# 5B
###B#.#C#A###
  #D#.#B#A#
  #D#.#A#C#
  #C#.#B#A#
  #########


#############
#.C.......DD# 6B
###B#.#C#A###
  #D#.#B#A#
  #D#.#A#C#
  #C#B#B#A#
  #########


#############
#.C.......DD# 4C
###.#.#C#A###
  #D#.#B#A#
  #D#B#A#C#
  #C#B#B#A#
  #########



#############
#.C.C.....DD# 6B
###.#.#.#A###
  #D#.#B#A#
  #D#B#A#C#
  #C#B#B#A#
  #########


#############
#.C.C.....DD# 4A
###.#.#.#A###
  #D#B#.#A#
  #D#B#A#C#
  #C#B#B#A#
  #########


#############
#.C.C...A.DD# 7B
###.#.#.#A###
  #D#B#.#A#
  #D#B#.#C#
  #C#B#B#A#
  #########

#############
#.C.C...A.DD# 7C
###.#B#.#A###
  #D#B#.#A#
  #D#B#.#C#
  #C#B#.#A#
  #########


#############
#.C.....A.DD# 8C
###.#B#.#A###
  #D#B#.#A#
  #D#B#.#C#
  #C#B#C#A#
  #########


#############
#.......A.DD# 4D
###.#B#.#A###
  #D#B#.#A#
  #D#B#C#C#
  #C#B#C#A#
  #########


#############
#D......A.DD# 4D
###.#B#.#A###
  #.#B#.#A#
  #D#B#C#C#
  #C#B#C#A#
  #########


#############
#DD.....A.DD# 10C
###.#B#.#A###
  #.#B#.#A#
  #.#B#C#C#
  #C#B#C#A#
  #########


#############
#DD.....A.DD# 9A
###.#B#.#A###
  #.#B#C#A#
  #.#B#C#C#
  #.#B#C#A#
  #########


#############
#DD.......DD# 10 A
###.#B#.#A###
  #.#B#C#A#
  #.#B#C#C#
  #A#B#C#A#
  #########


#############
#DD.......DD# 10 A
###.#B#.#.###
  #.#B#C#A#
  #A#B#C#C#
  #A#B#C#A#
  #########


#############
#DD.......DD# 6C
###.#B#.#.###
  #A#B#C#.#
  #A#B#C#C#
  #A#B#C#A#
  #########


#############
#DD.......DD#  11A
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#.#
  #A#B#C#A#
  #########


#############
#DD.......DD# 5D 5D 9D 9D
###A#B#C#.###
  #A#B#C#.#
  #A#B#C#.#
  #A#B#C#.#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

"""

print('Part 2', 7 * d + c * 5 + 4 * b + 9 * d + 5 * b + 6 * b + 4 * c + 6 * b + 4 * a + 7 * b + 7 * c + 8 * c + 4 * d + 4 *d + 10 * c + 9 * a + 10 * a + 10 * a + 6 * c + 11 * a + 28 * d)


def tmp():
    energy = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }


    # 0 is the one that can exit
    room_a = ['B', 'C']
    room_b = ['D', 'D']
    room_c = ['C', 'B']
    room_d = ['A', 'A']
    hallway = list('' * 11)



    min_energy = 999999999

    @lru_cache
    def solve(room_a, room_b, room_c, room_d, hallway, energy):
        if  room_a[0] == 'A' and room_a[1] == 'A' and \
            room_b[0] == 'B' and room_b[1] == 'B' and \
            room_c[0] == 'C' and room_c[1] == 'C' and \
            room_d[0] == 'D' and room_d[1] == 'D':

                return min_energy

        # check possible moves from hallway
        for i, amphipod in enumerate(hallway):
            if amphipod == '':
                continue
            if amphipod == 'A':
                if room_a[1] == 'A' and room_a[0] == '':
                    # move from hallway to the first position (closer to exit) in room A
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(2 - i) + 1) * energy['B']
                    return solve(['A', 'A'], room_b, room_c, room_d, new_hallway, energy + move_energy)
                elif room_a[1] == '':
                    # move from hallway to the second position (farther from exit) in room A
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(2 - i) + 2) * energy['A']
                    return solve(['', 'A'], room_b, room_c, room_d, new_hallway, energy + move_energy)
            elif amphipod == 'B':
                if room_b[1] == 'B' and room_b[0] == '':
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(4 - i) + 1) * energy['B']
                    return solve(room_a, ['B', 'B'], room_c, room_d, hallway, energy + move_energy)
                elif room_b[1] == '':
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(4 - i) + 2) * energy['B']
                    return solve(room_a, ['', 'B'], room_c, room_d, new_hallway, energy + move_energy)
            elif amphipod == 'C':
                if room_c[1] == 'C' and room_c[0] == '':
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(6 - i) + 1) * energy['C']
                    return solve(room_a, room_b, ['C', 'C'], room_d, hallway, energy + move_energy)
                elif room_c[1] == '':
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(6 - i) + 2) * energy['C']
                    return solve(room_a, room_b, ['', 'C'], room_d, new_hallway, energy + move_energy)
            elif amphipod == 'D':
                if room_d[1] == 'D' and room_d[0] == '':
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(8 - i) + 1) * energy['D']
                    return solve(room_a, room_b, room_c, ['D', 'D'], hallway, energy + move_energy)
                elif room_d[1] == '':
                    new_hallway = hallway[:]
                    new_hallway[i] = ''
                    move_energy = (abs(8 - i) + 2) * energy['D']
                    return solve(room_a, room_b, room_c, ['', 'D'], new_hallway, energy + move_energy)

        # check possible moves from room A
        if room_a[1] != 'A':
            if room_a[0] != '':

                for i, amphipod in enumerate(hallway):
                    if amphipod != '':
                        continue
