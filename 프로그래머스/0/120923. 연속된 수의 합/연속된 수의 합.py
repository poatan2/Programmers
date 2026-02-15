def solution(num, total):
    answer = []
    
    median = total // num

    if num%2==1:
        min = median - num//2
        for i in range(num):
            answer.append(min+i)

    else:
        min = median - num//2+1
        for i in range(num):
            answer.append(min+i)


   # print(answer)

    return answer