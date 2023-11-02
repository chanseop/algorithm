import sys

input=sys.stdin.readline
cnt=0

def hanso(x:int):
  if x<100:
    return True
  else:
    n=str(x)
    if int(n[0])-int(n[1]) == int(n[1])-int(n[2]):
      return True
    else:
      return False

N=int(input())

for i in range(1,N+1):
  if hanso(i):
    cnt+=1

print(cnt)