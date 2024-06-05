import sys

input = sys.stdin.readline

arr = list(input().rstrip())

newArr = []
ele = []
numberString = ""

# 숫자와 연산자를 분리하여 배열에 저장
for i in arr:
    if i == "-" or i == "+":
        newArr.append(int(numberString))
        ele.append(i)
        numberString = ""
    else:
        numberString += i
newArr.append(int(numberString))

answer = newArr[0]
minusNumber = 0
subtracting = False

for i in range(len(ele)):
    if ele[i] == "-":
        if subtracting:
            answer -= minusNumber
        else:
            answer += minusNumber
        minusNumber = newArr[i + 1]
        subtracting = True
    else:
        if subtracting:
            minusNumber += newArr[i + 1]
        else:
            answer += newArr[i + 1]

# 마지막으로 처리되지 않은 minusNumber를 처리
if subtracting:
    answer -= minusNumber

print(answer)
