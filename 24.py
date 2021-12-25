import fileinput

def parse():
    instr = []
    for line in fileinput.input():
        split = line.strip().split()
        instr.append(split)

    return instr

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def process(input, instructions):
    input_idx = 0
    alu = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for instruction in instructions:
        # print(instruction)
        instr = instruction[0]

        if instr == 'inp':
            print(alu)
            print(input[input_idx])

            alu[instruction[1]] = int(input[input_idx])
            input_idx += 1
        else:
            a = alu[instruction[1]]
            b = int(instruction[2]) if check_int(instruction[2]) else alu[instruction[2]]

            if instr == 'add':
               alu[instruction[1]] = a + b
            elif instr == 'mul':
                alu[instruction[1]] = a * b
            elif instr == 'div':
                if b == 0:
                    return None
                alu[instruction[1]] = a // b
            elif instr == 'mod':
                if a < 0 or b <= 0:
                    return None
                alu[instruction[1]] = a % b
            elif instr == 'eql':
                alu[instruction[1]] = 1 if a == b else 0

    return alu


# Very hard and weird
# Solved in a workbook, thanks to https://github.com/mrphlip/aoc/blob/master/2021/24.md and other stuff on reddit....

# part 1
instr = parse()
print(process(list('49917929934999'), instr))

# part 2
print(process(list('11911316711816'), instr))
