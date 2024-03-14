import sys
import math

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
maxGCD = 0
for i in range(0,1001):
    newArr = list(map(lambda x:x-i ,arr))
    gcd = math.gcd(*newArr)
    if maxGCD < gcd:
        maxGCD = gcd

print(maxGCD)