import heapq
import sys

input = sys.stdin.readline

n = int(input())

queue = []

for i in range(n):
    a = int(input())
    if a == 0 and len(queue) == 0:
        print(0)
    elif a == 0 and len(queue)>0:
        popnumber = heapq.heappop(queue)
        print(popnumber)
    else:
        heapq.heappush(queue,a)