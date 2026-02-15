def solution(bin1, bin2):
    answer = ''

    # 1. 길이를 맞춘다.
    maxLen = 0
    if len(bin1) > len(bin2):
        maxLen = len(bin1)
        bin2 = bin2.zfill(len(bin1))   # 큰 숫자에 맞춰 부족한 자리수를 0으로 채움
    else:
        maxLen = len(bin2)
        bin1 = bin1.zfill(len(bin2))


    carry = 0
    # 2. 뒤에서부터 계산 (2진수 덧셈)
    for i in range(maxLen-1,-1,-1):
        temp = int(bin1[i]) + int(bin2[i]) + carry
        carry = 0

        if temp == 2:
            carry = 1
            temp = 0
        if temp == 3:
            temp = 1
            carry = 1

        answer += str(temp)
    
    # 3. 마지막 자리수에 carry 존재한다면 올림 처리
    if carry == 1:
        answer +="1"
   

    # 4. 2진수니까 뒤집어서 합치기
    answer = "".join(answer[::-1])
    
    
    
    return answer