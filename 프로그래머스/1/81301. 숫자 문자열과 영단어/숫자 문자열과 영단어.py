def solution(s):
    answer = '' # 초기화 시 공백을 넣으면 안된다 ' '금지
    temp =''
    
    dict_num = { 'zero':'0', 'one':'1','two':'2', 'three':'3', 'four':'4','five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in dict_num:
                answer+=dict_num[temp]
                temp=''
                
    answer = int(answer)
    return answer
