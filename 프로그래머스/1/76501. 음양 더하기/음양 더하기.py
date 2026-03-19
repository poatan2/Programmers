def solution(absolutes, signs):
    answer = 0
    cnt = 0
    
    for i in signs:
        if i == True:   # 불리언 배열
            answer += absolutes[cnt]
        else:
            answer -= absolutes[cnt]
        cnt +=1
        
    return answer