n=int(input())
str_list=[]
str_len=[]
result=[]
for i in range(n):
    str_list.append(input())

for i in range(len(str_list)):
    if len(str_list[i]) not in str_len:
        str_len.append(len(str_list[i]))
str_len.sort()

# print(str_len)

for i in str_len:
    li=[]
    for j in range(len(str_list)):
        if i ==len(str_list[j]):
            li.append(str_list[j])
    li.sort()
    result+=li

answer=[]
for i in result:
    if i not in answer:
        answer.append(i)

for i in answer:
    print(i)