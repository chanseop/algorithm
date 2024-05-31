import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def bfs(x, y,arr,visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y]=True
    dx = [0,0,1,-1]
    dy = [1,-1,0, 0]

    while(queue):
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if not(0<=nx<n and 0<=ny<m) or arr[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            queue.append((nx,ny))
            visited[nx][ny]=True 
    return True


for i in range(t):
    m , n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    cnt = 0 
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1 and visited[x][y] == False:
                if bfs(x,y,arr,visited):
                    cnt +=1
    # print(arr)
    # print(visited)
    print(cnt)

