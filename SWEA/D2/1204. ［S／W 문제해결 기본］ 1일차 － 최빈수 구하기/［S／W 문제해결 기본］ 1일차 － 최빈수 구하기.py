case = int(input())

for i in range(case):
    tn = int(input())
    arr = list(map(int,input().split()))

    dp = [0]*101
    for j in range(len(arr)):
        dp[arr[j]] += 1
    maxCount = max(dp)
    filterArr =[]
    for x,count in enumerate(dp):
        if dp[x] == maxCount:
            filterArr.append(x)
    result = max(filterArr)
    print(f"#{tn} {result}")