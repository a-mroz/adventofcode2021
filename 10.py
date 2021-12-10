import fileinput


input = [l.strip() for l in fileinput.input()]

invalid = []
points = 0

for l in input:
    stack = []

    for char in l:
        if char == '{' or char == '(' or char == '<' or char == '[':
            stack.append(char)
        elif char == '}':
            if stack.pop() != '{':
                invalid.append('}')
                points += 1197
                break
        elif char == ')':
            if stack.pop() != '(':
                invalid.append(')')
                points += 3
                break
        elif char == '>':
            if stack.pop() != '<':
                invalid.append('>')
                points += 25137
                break
        elif char == ']':
            if stack.pop() != '[':
                invalid.append(']')
                points += 57
                break
        else:
            print('invalid character', char)

print(points)
