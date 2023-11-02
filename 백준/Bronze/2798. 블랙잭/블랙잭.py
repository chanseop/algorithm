n,m = map(int,input().split())
arr=list(map(int,input().split()))
first_sum=[]
result=[]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            first_sum.append(arr[i]+arr[j]+arr[k])

first_sum.sort()
for i in first_sum:
    if i<=m:
        result.append(i)

print(result[-1])