def solution(numbers):
    answer = 45 #1부터9까지 더한 합
    
    for i in numbers:
        answer -= i # 1부터9까지 더한 값중 없는 수만 뺌
    return answer