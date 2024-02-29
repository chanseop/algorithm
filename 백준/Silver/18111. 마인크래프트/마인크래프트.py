import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

arr = []

for i in range(n):
    arr.extend(map(int, input().split()))


def calc_time(h, arr, b):
    time = 0
    blocks = b

    for height in arr:
        if h > height:
            time += h - height
            blocks -= h - height
        elif h < height:
            time += 2 * (height - h)
            blocks += height - h

    if blocks >= 0:
        return time
    else:
        return float('inf')  # 불가능한 경우를 나타내기 위해 무한대 값 반환


min_time = float('inf')
max_height = 0

for h in range(257):  # 0부터 256까지의 각 높이에 대해 시간 계산
    total_time = calc_time(h, arr, b)

    if total_time <= min_time:
        min_time = total_time
        max_height = h

print(min_time, max_height)
