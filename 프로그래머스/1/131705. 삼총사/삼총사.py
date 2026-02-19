def solution(number):
    answer = 0
    
    # 그냥 중요한건 for문을 어디까지 돌릴지
    # 1번은 마지막 2개는 선택하면 안됨. 그러면 2번, 3번 숫자들은 out of index니까
    # 2번은 마지막 1개는 선택하면 안됨.
    
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                if number[i]+number[j]+number[k] == 0:
                    answer+=1
                
    return answer