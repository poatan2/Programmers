import math


def solution(a, b):
    answer = 0

    # 유한소수가 되기 위한 분수의 조건
    # "기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다."
    # * 정수도 유한소수로 분류한다. *


    # 1. a/b를 기약 분수로 만들자

    # 최대 공약수 찾기
    gcd_value = math.gcd(a,b)

    # 최대 공약수로 나누기
    ga = a // gcd_value
    gb = b // gcd_value
    
    if gb == 1: # 분모가 1이면 정수나끼 유한소수라고 판별
        answer =1
        return answer
    
    # 2. 분모의 소인수를 구하자
    check = False

    while gb > 1:
        if gb % 2 == 0:
            check = True
            gb = gb // 2
        elif gb % 5 ==0:
            check = True
            gb = gb // 5
        else:
            check = False
            break
            
   
    
    if check == True:
        answer = 1
    else:
        answer = 2

    return answer


