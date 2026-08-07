def solution(s):
    answer = 0
    
    cnt_x=0     # x가 나온 횟수
    cnt_nox=0   # x가 아닌 글자가 나온 횟수
    
    x=s[0]
    
    for i in s:
        # 1. 횟수 카운팅
        if i == x:
            cnt_x+=1
        else:
            cnt_nox+=1
            
        # 2. 문자열 맨 앞에 제거
        if len(s) != 1:
            s=s[1:]
            
        # 3. 횟수가 같은 경우
        if cnt_x == cnt_nox:
            answer+=1
            x=s[0]
            cnt_x=0
            cnt_nox=0

    # 4. 더 이상 읽을 글자가 없을 때
    if cnt_x or cnt_nox:
        answer+=1
    
    return answer