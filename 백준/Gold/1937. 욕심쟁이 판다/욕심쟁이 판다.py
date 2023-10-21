import sys

sys.setrecursionlimit(10**6)


n=int(input())
graph=[]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
memo=[[-1] * n for _ in range(n)]
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().strip().split())))

def dfs(x,y):
  if memo[x][y] == -1:
    memo[x][y]=1
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and graph[x][y]<graph[nx][ny]:
        memo[x][y] = max(memo[x][y], dfs(nx,ny) + 1)
  return memo[x][y]
  
res=0
for row in range(n):
  for col in range(n):
    res=max(res,dfs(row,col))

print(res)