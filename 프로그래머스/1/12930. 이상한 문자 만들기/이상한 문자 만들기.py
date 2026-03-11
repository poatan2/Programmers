def solution(s):
    answer = ''
    
    loc = 0
    for i in s:
        if i == ' ':
            loc = 0
            answer += ' '
        else:
            if loc%2 == 0:
                answer+=i.upper()
            else:
                answer+=i.lower()
            loc +=1
    
    
    
    
    return answer