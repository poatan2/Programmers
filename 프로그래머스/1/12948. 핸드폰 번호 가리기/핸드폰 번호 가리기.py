def solution(phone_number):
    answer = ''
    cnt=1
    
    for i in phone_number:
        if cnt < len(phone_number)-3:
            answer+='*'
        else:
            answer+=i
        cnt+=1
    
    
    return answer