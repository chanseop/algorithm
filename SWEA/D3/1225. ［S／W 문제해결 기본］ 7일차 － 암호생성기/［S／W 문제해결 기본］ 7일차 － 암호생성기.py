from collections import deque

for _ in range(1, 11):
    case = int(input())
    arr = deque(map(int, input().split()))

    i = 1
    while True:
        # 감소 주기: 1 ~ 5
        if i > 5:
            i = 1

        # 첫 번째 요소 가져와서 감소
        tmp = arr.popleft() - i
        if tmp <= 0:
            arr.append(0)
            break
        arr.append(tmp)

        # 감소 값 증가
        i += 1

    # 결과 출력
    result = " ".join(map(str, arr))
    print(f"#{case} {result}")

