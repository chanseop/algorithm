case = int(input())

for i in range(case):
    n = int(input())
    arr = list(map(int , input().split()))
    maxNumber = max(arr)
    result = 0
    for j in range(n):
        if(arr[j]==maxNumber and j!=n-1):
            # maxNumber change
            maxNumber = max(arr[j+1:])

        if(arr[j]<maxNumber):
            result += maxNumber-arr[j]

    print(f"#{i+1} {result}")