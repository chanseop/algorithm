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

for testCase in range(1,11):
    n = int(input())
    arr=[list(input()) for _ in range(8)]
    arr2=[]

    for i in range(8):
        newArr =[]
        for j in range(8):
            newArr.append(arr[j][i])
        arr2.append(newArr)

    # print(arr)
    # print(arr2)

    result=0
    for i in range(8):
        newArr=arr[i]
        newArr2=arr2[i]
        for j in range(9-n):
            sliceArr = newArr[j:j+n]
            sliceArr2 = newArr2[j:j+n]
            result += check(n,sliceArr) + check(n,sliceArr2)

    print(f"#{testCase} {result}")



