def solution(n):
    answer = 0
    
    big = n + 1
    bin_n = ''
    
    while True:             # n의 2진수 구하기
        bin_n+=(str(n%2))
        n = n //2
        
        if n == 0:
            break

    cnt1 = bin_n.count('1') # 구한 2진수에서 1의 개수 구하기
    
    m = big     # n보다 큰 값인 m
    bin_m = ''  

    while True:
        while True: # m의 2진수 구하기
            bin_m +=(str(m%2))
            m = m //2
          
            if m == 0:
                break
        
        if bin_m.count('1') == cnt1:    # cnt1과 m의 2진수의 1의 개수랑 같으면 끝
            answer = big
            return answer
        
        else:                       # 같지 않으면 m + 1
            big = big + 1
            m = big
            bin_m = ''
            
