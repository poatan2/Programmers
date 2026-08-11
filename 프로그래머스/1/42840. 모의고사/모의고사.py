def solution(answers):
    answer = []
    
    arr1=[1,2,3,4,5]
    arr2=[2,1,2,3,2,4,2,5]
    arr3=[3,3,1,1,2,2,4,4,5,5]
    
    idx=0
    cnt_dict={1:0,2:0,3:0}
    
    for i in answers:
        if arr1[idx%5] == i:
            cnt_dict[1]+=1
        if arr2[idx%8] == i:
            cnt_dict[2]+=1
        if arr3[idx%10] == i:
            cnt_dict[3]+=1
        idx+=1

        
    answer.append(1)
    if cnt_dict[2]>cnt_dict[answer[0]]:
        answer.pop()
        answer.append(2)
    elif cnt_dict[2] == cnt_dict[answer[0]]:
        answer.append(2)
    if cnt_dict[3]>cnt_dict[answer[0]]:
        answer.pop()
        answer.append(3)
    elif cnt_dict[3] == cnt_dict[answer[0]]:
        answer.append(3)
    
    
    """max함수를 이용해서 가장 큰 값을 가진 키만 구하고
    싶지만 방법을 모름.."""
    
    return answer