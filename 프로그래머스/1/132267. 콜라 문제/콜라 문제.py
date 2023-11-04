def solution(a, b, n):
    ans = 0  
    while n>=a:
        ans +=b
        n= n-a+b
    
    return ans
