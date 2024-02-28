import sys

input = sys.stdin.readline

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)
n = int(input())
if n!=0:
    problemLevelArr = []
    for i in range(n):
        problemLevel = int(input())
        problemLevelArr.append(problemLevel)

    removeIdx = my_round(n*0.15)
    problemLevelArr.sort()
    removeIdxArr = problemLevelArr[removeIdx:n-removeIdx]

    print(my_round(sum(removeIdxArr)/len(removeIdxArr))) 
else:
    print(0)
