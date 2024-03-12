import sys

input = sys.stdin.readline

c = int(input())
n = int(input())

graph = [[] for _ in range(c+1)]

for i in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(c+1)

def dfs(start):
    global visited
    visited[start] = True

    for next_node  in graph[start]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)

print(sum(visited)-1)
