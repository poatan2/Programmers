def solution(n):
    answer = 0
    
    # 3진법은  3으로 나눌 수 없을 때까지 3으로 나누고, 나머지를 거꾸로 읽으면 됨.
    
    ternary = [] # 3진법을 담을 배열
    
    # 아래의 반복문 처럼 작성하면 앞뒤반전된 3진법이 출력된다.
    while True:
        ternary.append(n % 3)
        n = n // 3
            
        if n == 0:
            print(ternary)
            break 
            
    # 다시 10진법으로 바꾸기
    # 0,0,2,1 이 있으면 0번째 인덱스에 3**3을 넣어줘야 하니까
    # 계산하기 편하게 reverse를 시켜주자
    ternary.reverse() 
    for i in range(len(ternary)-1,-1,-1):
        answer+= (3**i)*ternary[i]
    
    
    return answer