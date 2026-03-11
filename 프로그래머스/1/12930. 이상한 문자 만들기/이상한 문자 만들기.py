def solution(s):
    answer = ''
    
    loc = 0     #자릿수를 나타낼 변수
    
    for i in s:
        if i == ' ':    # 공백이라면 loc를 0으로 초기화
            loc = 0
            answer += ' '   
        else:           # 문자가 보이면 대소문자로 바꾸는 로직
            if loc%2 == 0:  
                answer+=i.upper()
            else:
                answer+=i.lower()
            loc +=1
    
    return answer
