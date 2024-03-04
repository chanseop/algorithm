import sys

input =  sys.stdin.readline

n,m = map(int,input().split())

dont = set()
answer = []

for i in range(n+m):
    string = input().rstrip()
    if string in dont:
        answer.append(string)
    else:
        dont.add(string)

answer.sort()
print(len(answer))
for i in answer:
    print(i)