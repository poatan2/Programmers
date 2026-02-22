def solution(numbers):
    answer = 0
    
    words=  ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    #enumerate는 파이썬에서 반복문을 돌릴 때 **"현재 몇 번째 바퀴인지(인덱스)"**와 **"그 안에 들어있는 값"**을 동시에 가져오고 싶을 때 사용하는 아주 유용한 함수입니다
    for i, word in enumerate(words):
        # 문자열.replace(찾을값, 바꿀값)
        # 따라서 문자열에 "one" 있으면 모든 "one"을 str(1)로 변환
        numbers = numbers.replace(word,str(i))
    
    answer = int(numbers)
    
    
    return answer