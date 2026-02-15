def solution(x, n):
    answer = []
    cnt = 1
    num = x
    
    while cnt <= n:
        answer.append(num)
        num += x
        cnt += 1
        
    return answer