def solution(array, commands):
    answer = []
    
    arr =[]
    
    for com in commands:
        i = com[0]-1
        j = com[1]
        k = com[2]-1
        
        arr = array[i:j]
        arr.sort()
        print(arr)
        answer.append(arr[k])
        
    return answer