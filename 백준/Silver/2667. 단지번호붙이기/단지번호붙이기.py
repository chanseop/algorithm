import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr =[]

for i in range(n):
    inputList = list(map(int,input().rstrip()))
    arr.append(inputList)

visited = [[False for _ in range(n)] for _ in range(n)]

result = []
# print(arr)
# print(visited)
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 1

    while(queue):
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if not(0<=nx<n and 0<=ny<n) or visited[nx][ny] == True or arr[nx][ny] == 0:
                continue
            queue.append((nx,ny))
            visited[nx][ny] = True
            count += 1

    return count

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and visited[i][j]==False:
            result.append(bfs(i,j))


print(len(result))
result.sort()
for answer in result:
    print(answer)