def solution(str1, str2):
    answer = 0
    
    
    for i in range(0, len(str1)):
        if (str1[i:i+len(str2)]==str2):
            answer = 1
            break
        else:
            answer = 2
            
    
    return answer
