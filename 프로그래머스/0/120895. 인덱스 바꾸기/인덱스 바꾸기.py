def solution(my_string, num1, num2):
    answer = ''
    cnt = 0
    for i in my_string:
        if cnt == num1:
            answer+=my_string[num2]
        elif cnt == num2:
            answer += my_string[num1]
        else:
            answer += i
        cnt+=1
    
    
    return answer