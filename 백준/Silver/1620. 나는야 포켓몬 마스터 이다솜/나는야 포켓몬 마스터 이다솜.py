import sys

input = sys.stdin.readline

n,m = map(int, input().split())

book = dict()
for i in range(1,n+1):
    string = input().rstrip()
    book[i] = string
    book[string] = i


for i in range(m):
    problem = input().rstrip()
    if problem.isdecimal():
        print(book[int(problem)])
    else:
        print(book[problem])