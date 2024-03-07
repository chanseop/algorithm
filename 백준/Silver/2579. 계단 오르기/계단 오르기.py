n = int(input())

stair = [0 for _ in range(n+1)]

for i in range(n):
    stair[i] = int(input())

dp = [0 for _ in range(n+1)]

dp[0] = stair[0]
if n > 1:
    dp[1] = stair[0] + stair[1]
if n > 2:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3,n):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[n-1])