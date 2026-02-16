def solution(my_string):
    answer = ''
    
    lower= my_string.lower()
    
    answer = ''.join(sorted(lower))
    return answer