import sys

input =  sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break

    stack = []
    answer = True
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = False
                break
    if stack:
        answer = False
    print('yes' if answer else 'no')
    