def solution(k, score):
    answer = []
    
    #hall of fame
    hof = []
    
    for num in score:
        hof.append(num)
        hof.sort(reverse=True)
        
        if len(hof) > k:
            hof.pop()
        
        answer.append(min(hof))
        
    
    return answer