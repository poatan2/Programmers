def solution(quiz):
    answer = []
    
    num1 = 0
    num2 = 0
    operator = ''
    

    for j in quiz:
        # 아래와 같이 공백으로 나누어 새로운 배열로 만든다.
        # "3 - 4 = -3" -> ['3','-','4','=','-3']
        # 이렇게 하여 배열의 요소로 접근
        uquiz = j.split()   
        
        num1 = int(uquiz[0])
        num2 = int (uquiz[2])
        operator = uquiz[1]
        result = int(uquiz[4])
            
        if operator == '+':
            res = num1+num2
        else:
            res = num1-num2
        
        if res == result:
            answer.append("O")
        else:
            answer.append("X")
                
    return answer