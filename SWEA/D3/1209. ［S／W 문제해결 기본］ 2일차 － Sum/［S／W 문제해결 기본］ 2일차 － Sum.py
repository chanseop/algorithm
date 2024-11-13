for _ in range(1, 11):
    testCase = int(input())
    arr = []
    for i in range(100):
        inputArr = list(map(int, input().split()))
        arr.append(inputArr)

    maxResult = 0

    cross1 = 0
    cross2 = 0

    # 행, 열, 대각선 합을 한 번에 계산
    for i in range(100):
        rowSum = sum(arr[i])            # i번째 행의 합
        colSum = sum(arr[j][i] for j in range(100))  # i번째 열의 합

        cross1 += arr[i][i]             # 왼쪽 위 -> 오른쪽 아래 대각선
        cross2 += arr[i][99-i]          # 오른쪽 위 -> 왼쪽 아래 대각선

        # 행과 열의 최대값을 갱신
        maxResult = max(maxResult, rowSum, colSum)

    # 대각선의 최대값을 갱신
    maxResult = max(maxResult, cross1, cross2)

    print(f"#{testCase} {maxResult}")
