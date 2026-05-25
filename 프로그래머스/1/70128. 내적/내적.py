def solution(a,b):
    answer=0
    arr=[]
    for i in range(0,len(a)):
        arr.append(a[i]*b[i])

    for i in arr:
        answer+=i

    return answer