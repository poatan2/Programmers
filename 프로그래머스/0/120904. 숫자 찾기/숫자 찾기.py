def solution(num, k):
    answer = 0
    
    str_num = str(num)
    
    cnt = 1
    
    for i in str_num:
        if int(i) == k:
            answer = cnt
            return answer
        cnt+=1
    answer = -1
    
    
    
    return answer