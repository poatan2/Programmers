def solution(numbers):
    answer = []
    s = set()
    
    # set 자료형에 담고 list()로 반환
    
    for i in range(len(numbers)-1):     
        for j in range(i,len(numbers)-1):
            temp = numbers[i]+numbers[j+1]
            s.add(temp)
            temp = 0
    
    
    answer = list(s)
    answer.sort()
    
    return answer