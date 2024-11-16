t = int(input())


for testCase in range(1,t+1):
    n,m,k=map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    breakPoint = True
    for visitedTime in arr:
        if visitedTime<m:
            breakPoint = False
            break

    maxTime = max(arr)
    restProduct = 0
    for i in range(m,maxTime+1):
        if breakPoint == False:
            break
        if i%m==0:
            restProduct += k
        # print(arr)
        if i in arr:
            for j in arr:
                # print("restProduct:",restProduct)
                # print("j:",j)

                if i==j:
                    restProduct -=1
                    if restProduct == -1:
                        breakPoint = False
                        break

    # print(breakPoint)
    if breakPoint:
        print(f"#{testCase} Possible")
    else:
        print(f"#{testCase} Impossible")