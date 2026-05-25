# 약수의 개수를 구하는 함수
def cnt_divisor(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    
    return cnt
    
    
    
def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        cnt_div=0
        cnt_div = cnt_divisor(i)    
        if cnt_div % 2 == 0:
            answer+=i
        else:
            answer-=i
        
        
        
    return answer