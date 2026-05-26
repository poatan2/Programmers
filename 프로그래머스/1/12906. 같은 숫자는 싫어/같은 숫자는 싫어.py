def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in arr[1:]:
        answer.append(i)
        if answer[-2] == i:
            answer.pop()
        

    return answer