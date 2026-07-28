def solution(a, b, n):
    answer = 0
    
    cola = 0 #받은 콜라 수
    
    while n//a:
        cola = (n//a)*b
        n = n%a+cola    # 다음에 교환할 병의 수는 마트에서 교환하고 남은 병+ 교환해서 받은 병
        answer+= cola
    
    return answer