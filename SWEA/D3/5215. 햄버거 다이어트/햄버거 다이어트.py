# input
# 1
# 5 1000
# 100 200
# 300 500
# 250 300
# 500 1000
# 400 400

# ouput
#1 750

# 200+300+300
# 100+250+400 = 750
# 뒤에 숫자의 조합중에 최댓값이 되는 조합 찾기

def backtrack(idx,scoreValue,calValue):
    # if calValue<=maxCal:
    result.append(scoreValue)
    # print("sum-cal:",calValue)
    # print("sum-score:",scoreValue)
    # print(result)

    for i in range(idx,len(score)):
        # print("i:",i)
        scoreValue += score[i]
        calValue += cal[i]
        if(calValue<=maxCal):
            backtrack(i+1,scoreValue,calValue)
        scoreValue -= score[i]
        calValue -= cal[i]



testcase = int(input())
for testCase in range(testcase):
    menuCnt,maxCal = map(int,input().split())

    score = [] # 맛 점수
    cal = [] # 칼로리
    result = [] # 합

    # 값 넣기
    for i in range(menuCnt):
        scoreValue,calValue = map(int,input().split())
        score.append(scoreValue)
        cal.append(calValue)

    backtrack(0,0,0)
    # print(result)
    print(f"#{testCase+1} {max(result)}")