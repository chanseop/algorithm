import sys
from itertools import combinations

input = sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m = map(int,input().split())
    top = 1
    for i in range(m, m-n, -1):
        top *= i

    bottom =1
    for i in range(n,1,-1):
        bottom *= i
    print(int(top/bottom))