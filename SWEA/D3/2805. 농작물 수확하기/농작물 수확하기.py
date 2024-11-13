testCase = int(input())
for test_case in range(testCase):
    size = int(input())
    arr =[]
    for i in range(size):
        arr.append(list(map(int, list(input()))))

    mainIdx = size//2
    minus = 1
    result = 0
    for i in range(len(arr)):
        if(i<=mainIdx):
            # print(abs(mainIdx-i),abs(mainIdx+i)+1)
            result += sum(arr[i][abs(mainIdx-i):abs(mainIdx+i)+1])
        elif i==mainIdx+1:
            # print(abs(mainIdx-i),abs(i+mainIdx)-(i-mainIdx))
            result += sum(arr[i][abs(mainIdx-i):abs(i+mainIdx)-(i-mainIdx)])
        else:
            # print(abs(mainIdx-i),abs(i+mainIdx)-(i-mainIdx)-minus)
            result += sum(arr[i][abs(mainIdx-i):abs(i+mainIdx)-(i-mainIdx)-minus])
            minus+=1


    print(f"#{test_case+1} {result}")