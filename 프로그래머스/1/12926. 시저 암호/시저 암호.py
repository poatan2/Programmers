def solution(s, n):
    answer = ''
    
    for i in s:
        ascii_s = ord(i)
        if ascii_s == 32:
            answer += " "
            continue
        
        elif i.isupper():
            
            result = (ascii_s-65+n)%26 +65
        else:
            result = (ascii_s-97+n)%26 +97
        
        answer += chr(result)
    
    
    return answer