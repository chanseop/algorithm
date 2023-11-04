import math

def notDivisible (arr,num):
        for n in arr:
            if n % num ==0:
                return False
        return True

def solution(arrayA, arrayB):
    answer = 0
    gcd_a=arrayA[0]
    gcd_b=arrayB[0]
    for i in range(1,len(arrayA)):
        gcd_a=math.gcd(gcd_a,arrayA[i])
        gcd_b=math.gcd(gcd_b,arrayB[i])
    
    print(gcd_a, gcd_b)
    if notDivisible(arrayA, gcd_b):
        if answer<gcd_b:
            answer=gcd_b
            
    if notDivisible(arrayB, gcd_a):
        if answer<gcd_a:
            answer=gcd_a
    
        
    return answer