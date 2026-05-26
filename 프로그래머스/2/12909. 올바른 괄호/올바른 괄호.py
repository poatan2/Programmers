def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == '(':    # ( 면 스택에 추가
            stack.append(i)
        else:           # ) 면 검사 시작
            if len(stack) == 0: #비어 있다면 False 반환
                return False    
            else:               
                if stack[-1] =='(': # 안 비어 있고 마지막 요소가 ( 라면 짝을 이루므로 pop
                    stack.pop()   
                else:               # 이 아니라면 False 반환
                    return False
    
    if len(stack) != 0:     # 다 끝나고 stack에 ( 가 남아 있다면 False 반환
        return False        
    
    return True