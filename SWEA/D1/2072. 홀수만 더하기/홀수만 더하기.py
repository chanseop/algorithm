case = int(input())

for j in range(case):
    sum = 0
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        n=arr[i]
        if(n%2 == 1):
            sum += n

    print("#"+str(j+1)+" "+str(sum))
   