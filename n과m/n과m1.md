##  문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
## 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

```python
import sys
N,M=map(int,sys.stdin.readline().split(' '))

check_list=[False for _ in range(N+1)]
def backtrack(perList:list,M):
    if len(perList)==M:
        print(" ".join(map(str,perList)))
        return
    
    for i in range(1,N+1):
        if check_list[i]==False:
            perList.append(i)
            check_list[i]=True
            backtrack(perList,M)
            perList.pop()
            check_list[i]=False
            
        
perList=[]

backtrack(perList,M)
```

## 풀이방법
이 문제는 backtracking 방법으로 풀었다. 우선 재귀로 품에 있어서 탈출조건을 정의 해주었다. 그리고 탈출 조건이 만족하면 pop하여서 해당 사항을 빼내고 다음 숫자를 넣어서
계속 탐색을 하였다. 

문제에서 조건중에 중복제외라는 조건이 있기 때문에 check배열을 생성해서 들어가 있는 숫자는 true로 반환하였다.
