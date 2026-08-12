import sys
sys.setrecursionlimit(10**6)

memo = {}

def solution(n):
    answer = 0
    
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = solution(n-2)+solution(n-1)
    
    answer = memo[n] % 1234567
    
    return answer