import fileinput
from functools import lru_cache

map = """
#############
#...........#
###B#D#C#A###
  #C#D#B#A#
  #########

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



# Move both As to the left, put Ds into correct places, move c out so B can also move out, move both Bs to correct positions, move Cs to correct positions, move As to the correct positions
# 9 + 9 + 7000 + 7000 +  200 + 50 + 50 + 300 + 700 + 3 + 3 = 15324


#Move A



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
