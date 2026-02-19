def solution(num):
    answer = 0
    
    if num == 0:
        return 1
    
    while answer<500:
        if num == 1:
            return answer
        
        elif num%2==0:
            num /= 2
            answer+=1
        else:
            num = (num*3)+1
            answer+=1     
    
    answer = -1
    
    return answer