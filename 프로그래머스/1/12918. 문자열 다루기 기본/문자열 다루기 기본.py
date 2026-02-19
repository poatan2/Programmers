def solution(s):
    answer = True
    
    if len(s)==4 or len(s)==6:
        for i in s:
            if i.isdigit() == False: #정수인지 확인하는 함수
                return False
                
    else:
        return False
                
    
    return answer