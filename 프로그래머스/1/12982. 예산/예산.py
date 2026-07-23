def solution(d, budget):
    answer = 0
    
    d.sort()
    cnt = 0
    
    for i in d:
        if budget >= i:
            budget -= i
            cnt += 1
        else:
            break
    
    return cnt