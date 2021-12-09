import fileinput

input = []

for l in fileinput.input():
    ex = l.strip().split('|')
    input.append((ex[0].strip().split(), ex[1].strip().split()))

known_len = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


recognized_outputs = 0
for _, output in input:
    for d in output:
        if len(d) in known_len:
            recognized_outputs += 1

print(recognized_outputs)

# 2

# initial_mappings = {
#     0: 'abcefg',    #6
#     1: 'cf',        #2
#     2: 'acdeg',     #5
#     3: 'acdfg',     #5
#     4: 'bcdf',      #4
#     5: 'abdfg',     #5
#     6: 'abdefg',    #6
#     7: 'acf',       #3
#     8: 'abcdefg',   #7
#     9: 'abcdfg',    #6
# }


res = []

for signals, outputs in input:
    signals = [''.join(sorted(signal)) for signal in signals]
    outputs = [''.join(sorted(output)) for output in outputs]


    mapping = {}
    reverse_mapping = {}

    # first, find the known ones
    for s in signals:
        signal_len = len(s)
        if signal_len in known_len: # 1, 4, 7, 8
            signal_number = known_len[signal_len]
            mapping[s] = signal_number
            reverse_mapping[signal_number] = set(s)

    # print(mapping)
    # print(reverse_mapping)

    for s in signals:
        signal_len = len(s)
        signal_set = set(s)

        if signal_len in known_len:
            continue

        if signal_len == 6: # 0, 6, 9
            if not reverse_mapping[1].issubset(signal_set):
                mapping[s] = 6
            elif reverse_mapping[4].issubset(signal_set):
                mapping[s] = 9
            else:
                mapping[s] = 0
        elif signal_len == 5: # 2, 3, 5
            if reverse_mapping[1].issubset(signal_set):
                mapping[s] = 3
            elif (reverse_mapping[4] | signal_set) == reverse_mapping[8]:
                mapping[s] = 2
            else:
                mapping[s] = 5

    print(mapping)

    res.append(int(''.join([str(mapping[o]) for o in outputs])))


print(sum(res))
