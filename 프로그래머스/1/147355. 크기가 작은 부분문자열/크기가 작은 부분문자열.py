def solution(t, p):
    answer = 0
    
    p_len = len(p)
    
    for i in range(0,len(t)-p_len+1):   # p_len+1을 해야 t의 마지막 문자열까지 들어감.
        if int(t[i:i+p_len]) <= int(p):
            answer += 1
        
    return answer