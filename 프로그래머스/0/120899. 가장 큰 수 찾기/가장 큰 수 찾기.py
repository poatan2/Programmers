def solution(array):
    answer = []
    max = 0
    index = 0
    
    
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if(max<array[j]):
                max = array[j]
                index = j         
            
    answer.append(max)
    answer.append(index)
    return answer