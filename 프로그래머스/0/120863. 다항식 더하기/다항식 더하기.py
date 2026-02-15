def solution(polynomial):
    answer = ''
    
    x_sum = 0
    const_sum = 0

    # 모든 원소를 나눔
    dist = polynomial.split()

    for i in dist:
        if 'x' in i: # x항인지 확인
            # x를 떼고 바로 정수로 바꾸기
            temp = (i.replace("x", ""))
            if temp == "": # 계수가1인지 확인
                x_sum+=1
            else:
                x_sum+=int(temp)
            
        elif i.isdigit():
            const_sum+=int(i)
    
    # 결과 조립
    # 1x의 경우 x라고 출력
    # x항이나 상수항이 0일 경우 결과에 나타나면 안됨
    # 두 항이 모두 있을 때 가운데 + 기호를 넣어야 됨

    if x_sum and const_sum:
        if x_sum!=1:
            answer= str(x_sum)+'x '+'+ '+str(const_sum)
        else:
            answer='x '+'+ '+str(const_sum)
    else:
        if x_sum:
            if x_sum!=1:     
                answer=str(x_sum)+'x'
            else:
                answer='x'
        else:
            answer=str(const_sum)
            
    return answer