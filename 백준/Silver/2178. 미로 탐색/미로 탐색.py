import sys
from collections import deque

def bfs(graph,x,y,visited):
  queue =deque([(x,y)])
  visited[x][y]=True
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<= nx < n and 0<=ny<m and graph[nx][ny]==1 and not visited[nx][ny]:
        graph[nx][ny] = graph[x][y]+1
        visited[nx][ny]=True
        queue.append((nx,ny))



n,m=map(int,sys.stdin.readline().split())
graph=[]
visited=[[False]*m for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().strip())))



bfs(graph,0,0,visited)
print(graph[n-1][m-1])