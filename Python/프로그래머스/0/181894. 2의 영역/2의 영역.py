def solution(arr) :
    answer = []
    if 2 not in arr : 
        return [-1]
    else : 
        for i in range(0, len(arr)) : 
            if arr[i] == 2 : 
                answer.append(i)
    return arr[answer[0] : answer[-1] + 1]