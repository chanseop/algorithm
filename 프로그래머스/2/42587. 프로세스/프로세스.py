def solution(priorities, location):
    q=[ (i,p) for i,p in enumerate(priorities)]
    ans=0
    while q:
        idx,value = q.pop(0)
        if any(value<q[i][1] for i in range(len(q))):
            q.append((idx,value))
        else:
            ans += 1
            if idx==location:
                return ans
    
    return ans