T =10

for test_case in range(1,T+1):
    n = int(input())
    blocks = list(map(int,input().split()))
    for i in range(n):
      blocks.sort()
      blocks[0]+=1
      blocks[-1]-=1

    print(f"#{test_case} {max(blocks)-min(blocks)}")