def solution(A, B):
    answer = 0
    
    if A==B:
        return answer
    
    n = len(A)
    
    # A[-1] : 마지막 글자
    # A[:-1] : 마지막 글자를 제외한 나머지

    for i in range(n):
        A = A[-1]+A[:-1]
        if A==B:
            answer = i+1
            return answer
    answer = -1
    
    return answer