import sys

input = sys.stdin.readline 

n,m = map(int,input().split())

arr = list(map(int,input().split()))

addTree = [0]*(n+1)
cnt =1
for number in arr:
    addTree[cnt] = addTree[cnt-1] + number
    cnt+=1

for i in range(m):
    start, end = map(int, input().split())
    print(addTree[end] - addTree[start-1])