def solution(number, limit, power):
    answer = 0
    cnt_list = []   # 약수의 개수를 담을 리스트
    cnt=0
    
    # 약수의 개수
    for i in range(1,number+1):
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                if i // j != j:
                    cnt+=2
                else:
                    cnt+=1
        # limit을 초과하는지 확인
        if cnt>limit:
            cnt = power # 초과하면 power로 변경
        cnt_list.append(cnt)
        cnt=0
    
    
        
    # 결과 구하기
    answer = sum(cnt_list)
    
    
    
    return answer