def check(n,checkArr):
    breakPoint = 1
    if(n%2==0):
        for i in range(int(n/2)):
            if(checkArr[i] != checkArr[-(1+i)]):
                breakPoint=0
    else:
        for i in range(n//2):
            if(checkArr[i] != checkArr[-(1+i)]):
                breakPoint=0
    return breakPoint

for _ in range(1):
    testCase = int(input())
    arr=[list(input()) for _ in range(100)]
    arr2=[]
    for i in range(100):
        newArr =[]
        for j in range(100):
            newArr.append(arr[j][i])
        arr2.append(newArr)

    # print(arr)
    # print(arr2)

    result=0
    maxidx=0
    for n in range(100,-1,-1):
        for i in range(100):
            newArr=arr[i]
            newArr2=arr2[i]
            for j in range(101-n):
                sliceArr = newArr[j:j+n]
                sliceArr2 = newArr2[j:j+n]
                result += check(n,sliceArr) + check(n,sliceArr2)
        if result>1:
            maxidx = n+1
            break

    print(f"#{testCase} {maxidx}")



