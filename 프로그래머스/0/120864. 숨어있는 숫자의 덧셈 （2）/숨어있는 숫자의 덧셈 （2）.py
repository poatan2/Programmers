def solution(my_string):
    answer = 0
    temp = ''
    total = 0
    
    for i in my_string:
        if i.isdigit(): # 숫자인지 확인?
            temp += i
        else:  # 문자라면temp에 있는 값을 total에 넣기
            if temp != '': # 받아온 숫자가 있으면 total에 넣기
                total += int(temp)
                temp = ''
                
    # 만약 문자열이 숫자로 끝나면 마지막 temp는 문자를 만나지 못했으므로 total에 안들어감
    # 따라서 끝나고 temp의 값이 있다면 넣어주기
    if temp != '':
        total += int(temp)
        
    answer = total
    
    return answer