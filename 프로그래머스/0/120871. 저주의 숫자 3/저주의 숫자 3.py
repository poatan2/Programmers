def solution(n):
    answer = 0

    # 3의 배수와 숫자 3을 사용하지 않는다.
    
    # 그러면 숫자에서 검사해야 하는 것이
    # 1. 숫자 3이 들어가 있는지
    # 2. 3의 배수인지

    # 그러면 가장 먼저 드는 생각은 n을 카운팅 느낌으로 가져가보자
    # for 문에서 2가지의 검사 루틴이 순서가 서로 바뀌어 검사를 하도록 했다.
    # 1. 3의 배수여서 +1 했는데 안에 숫자 3이 있는 경우
    # 2. 반대로 숫자 3이 있어서 +1 했는데 3의 배수인 경우
    num=0
    
    for i in range(n):
        num +=1
        if num % 3 == 0:   
            num+=1
            if str(3) in str(num):  # num안에 3이 들어있는지 확인
                while str(3) in str(num):
                    num+=1
                
        elif str(3) in str(num):
            num+=1
            if num % 3 == 0:
                num+=1
        
    
    answer = num

    return answer