import fileinput


input = [l.strip() for l in fileinput.input()]

invalid = []
pointsCorrupted = 0
pointsIncomplete = []


incompletePunctation = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

for l in input:
    stack = []

    corrupted = False

    for char in l:
        if char == '{' or char == '(' or char == '<' or char == '[':
            stack.append(char)
        elif char == '}':
            if stack.pop() != '{':
                invalid.append('}')
                corrupted = True
                break
        elif char == ')':
            if stack.pop() != '(':
                invalid.append(')')
                corrupted = True
                break
        elif char == '>':
            if stack.pop() != '<':
                corrupted = True
                pointsCorrupted += 25137
                break
        elif char == ']':
            if stack.pop() != '[':
                pointsCorrupted += 57
                corrupted = True
                break
        else:
            print('invalid character', char)

    # 2
    if not corrupted > 0:
        print(stack)
        points = 0
        for char in reversed(stack):
            points = points * 5 + incompletePunctation[char]

        pointsIncomplete.append(points)


print(pointsCorrupted)
print(sorted(pointsIncomplete)[int(len(pointsIncomplete)/2)])
