import sys

input = sys.stdin.readline

t = int(input())

def p(n):
    whiteArr = [1,2,3]
    blueArr =  [1,1,2]
    for i in range(3,n+1):
        blueArr.append(whiteArr[i-1] + whiteArr[i-3]) 
        whiteArr.append(blueArr[i] + blueArr[i-2])
    
    if (n+1)%2 == 0:
        idx = (n+1) // 2
        print(whiteArr[idx-1])
    else:
        idx = n // 2
        print(blueArr[idx])

for i in range(t):
    n = int(input()) - 1
    p(n)