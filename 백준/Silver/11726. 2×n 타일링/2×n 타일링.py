import sys

input = sys.stdin.readline

n = int(input())

memo=[1]*n

if n>=2:
    memo[1]=2
    for i in range(2,n):
        memo[i] = memo[i-1] + memo[i-2] 

print(memo[-1]% 10007)