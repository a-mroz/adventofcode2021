import fileinput

input = []

for l in fileinput.input():
    ex = l.strip().split('|')
    input.append((ex[0].strip().split(), ex[1].strip().split()))

known_len = { 2: 1, 4: 4 , 3: 7, 7: 8}


recognized_outputs = 0
for _, output in input:
    for d in output:
        if len(d) in known_len:
            recognized_outputs += 1

print(recognized_outputs)