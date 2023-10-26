arr=[]          #문자 받기
arr_a=[]        #문자 걸러내기
arr_n=[]        #갯수
cnt=1
s=input()

for y in s:
    a=y.upper()
    arr.append(a)

for y in arr:
    if y in arr_a:
        x=arr_a.index(y)
        arr_n[x]+=1
    else:
        arr_a.append(y)
        arr_n.append(cnt)


max=max(arr_n)
count=0
for y in range(len(arr_n)):
    if max==arr_n[y]:
        count+=1

if count>1:
    print('?')
else:
    print(arr_a[(arr_n.index(max))])