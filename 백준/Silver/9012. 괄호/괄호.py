import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    answer =True

    string = input().rstrip()

    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack :
                stack.pop()
            else:
                answer = False
    if stack:
        answer = False
    print("YES" if answer else "NO")