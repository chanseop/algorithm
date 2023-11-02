n=int(input())
result=[]
sum_=0

for i in range(1,n+1):                          
    num_list=list(map(int,str(i)))    #숫자를 리스트에 한글자씩 넣기
    sum_=i+sum(num_list)                  #리스트 합 구하기
    if sum_==n:                       #생성자면 추가
        result.append(i)
        break
    if i==n:
        result.append(0)

result.sort()

answer=result[0]

print(answer)