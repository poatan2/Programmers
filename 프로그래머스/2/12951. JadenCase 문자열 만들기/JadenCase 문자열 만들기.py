def solution(s):
    answer = ''
    index = 0
    
    for i in s:
        if i == ' ': 
            answer +=' '
            index = 0
        elif index == 0:     
            if i.isdigit(): 
                answer += i
                index += 1
            else:           
                answer += i.upper()
                index += 1
        else:                
            answer += i.lower()
            index += 1
        
                    
    return answer