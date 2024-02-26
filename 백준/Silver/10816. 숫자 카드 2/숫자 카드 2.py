import sys

# 입력 받기
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
cards.sort()

# 이진 탐색을 이용하여 숫자 카드의 개수를 세는 함수
def count_cards(cards, target):
    left, right = 0, len(cards) - 1
    start, end = -1, -1

    # 이진 탐색을 통해 target의 시작 인덱스 찾기
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] >= target:
            if cards[mid] == target:
                start = mid
            right = mid - 1
        else:
            left = mid + 1

    left, right = 0, len(cards) - 1

    # 이진 탐색을 통해 target의 끝 인덱스 찾기
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] <= target:
            if cards[mid] == target:
                end = mid
            left = mid + 1
        else:
            right = mid - 1

    # 시작 인덱스와 끝 인덱스로 개수 계산
    if start != -1 and end != -1:
        return end - start + 1
    else:
        return 0

# 타겟 숫자별로 카드 개수를 세고 출력
result = []
for target in targets:
    result.append(count_cards(cards, target))

print(' '.join(map(str, result)))