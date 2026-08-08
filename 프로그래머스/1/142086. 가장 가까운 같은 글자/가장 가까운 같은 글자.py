def solution(s):
    answer = []
    
    # 처음 나온 문자열의 위치와 문자를 딕셔너리로 저장
    
    alpha={}
    index=1
    
    for i in s:
        # 딕셔너리에 문자가 없는 경우 새로 추가
        if i not in alpha:
            alpha[i]=index
            answer.append(-1)
        # 딕셔너리 이미 문자가 있을 경우
        else:
            answer.append(index-alpha[i])
            alpha[i]=index  # 이번 위치로 딕셔너리를 업데이트
        
        index += 1
            

    return answer