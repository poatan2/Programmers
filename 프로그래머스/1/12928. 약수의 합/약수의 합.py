def solution(n):
    answer = 0
    factor = [] #약수가 담길 배열
    num = 1     #약수 대기자들
    
    while num<=n:
        if n%num == 0: #약수면 배열에 추가
            factor.append(num)
            
        num+=1
        
    for i in range(len(factor)):
        answer += factor[i] #정답구하기
    
    return answer