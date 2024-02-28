import sys

input = sys.stdin.readline

n = int(input())

dex =  []
for i in range(n):
    command = list(input().split())
    if len(command) == 1:
        string = command[0]
        if string == "size":
            print(len(dex))
        elif string == "empty":
            print(1 if len(dex)==0 else 0)
        elif string == "pop_front":
            if len(dex) == 0:
                print(-1)
            else:
                popNumber = dex[0]
                dex = dex[1:]
                print(popNumber)
        elif string == "pop_back":
            if len(dex) == 0:
                print(-1)
            else:
                popNumber = dex.pop()
                print(popNumber)
        elif string == "front":
            print(-1 if len(dex)==0 else dex[0])
        elif string == "back":
            print(-1 if len(dex)==0 else dex[-1])
    else:
        string = command[0]
        if string == "push_front":
            appendNum = command[1]
            arr=[appendNum]+dex
            dex = arr
        elif string == "push_back":
            appendNum = command[1]
            dex.append(appendNum)
